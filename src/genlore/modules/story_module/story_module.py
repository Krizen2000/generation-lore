import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '1'
import tensorflow as tf
import numpy as np
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
# from nltk.tokenize import sent_tokenize as get_sentence_list
# from nltk import download as nltk_download
# nltk_download('punkt')


class Story_Module:
    def __init__(self):
        self.load_model_config()
        self.load_tokenizer()
        self.load_model()

    def load_model_config(self):
        self.model_config = {}
        self.model_config["do_sample"] = False 
        self.model_config["num_beams"] = 1 
        self.model_config["num_beam_groups"] = 2
        self.model_config["max_new_tokens"] = 1024
        self.model_config["max_length"] = 1024
        self.model_config["no_repeat_ngram_size"] = 2
        self.model_config["length_penalty"] = 1.
        self.model_config["temperature"] = 1.

    def load_tokenizer(self):
        self.tokenizer: GPT2Tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def load_model(self):
        self.model: TFGPT2LMHeadModel = TFGPT2LMHeadModel.from_pretrained("gpt2")

    def unload_tokenizer(self):
        del self.tokenizer
        self.tokenizer = None

    def unload_model(self):
        del self.model
        self.model = None

    def get_imp_tokens(self,tokens: np.ndarray):
        # Input tokens contains values of Input Ids
        # 1000 tokens as input would be preffered
        # Assuming each sentence to be of 40 Tokens
        tokens = tokens[0]
        token_size = len(tokens)
        new_token_list = []
        # Extracting first two sentences
        slice_size = (2*40)
        pos = 0
        new_tokens = tokens[pos:(pos+slice_size)]
        new_token_list.append(new_tokens)
        # Extracting middle three sentences
        slice_size = (3*40)
        pos = token_size//2
        new_tokens = tokens[pos:(pos+slice_size)]
        new_token_list.append(new_tokens)
        # Extracting last four sentences
        slice_size = (4*40)
        pos = token_size - slice_size - 1
        new_tokens = tokens[pos:(pos+slice_size)]
        new_token_list.append(new_tokens)
        processed_tokens = np.concatenate(new_token_list,axis=0)
        processed_tokens = np.array([processed_tokens],np.int32)
        # print(f"[processed_tokens]: {processed_tokens}")
        return processed_tokens

    def valid_input_size(self,text):
        tokens = self.tokenizer.encode_plus(
            (self.tokenizer.eos_token + text),
            padding="max_length",
            return_attention_mask=False,
            return_token_type_ids=False,
            return_tensors="np",
        )
        if len(tokens["input_ids"][0]) > 400:
            return False
        return True

    def generate_attention_mask(self,tokens: np.ndarray):
        tokens = tokens[0]
        mask_list= np.array([],np.int64)
        print(f"[tokens]: {tokens}")
        print(f"[len(tokens)]: {len(tokens)}")

        for index in range(len(tokens)):
            if tokens[index] != self.tokenizer.eos_token_id:
                mask_list = np.append(mask_list,[1],axis=0)
                continue
            mask_list = np.append(mask_list,[0],axis=0)
        print(f"[mask_list]: {mask_list}")
        mask_list = np.array([mask_list],np.int32)
        return mask_list

    def encode_text(self,text,chunk_size=400):
        tokens = self.tokenizer.encode_plus(
            (self.tokenizer.eos_token + text),
            add_special_tokens=False,
            return_attention_mask=True,
            return_token_type_ids=False,
            return_tensors="np",
        )
        # print(f"[tokens]:{tokens}")
        # print(f"[type(tokens)]:{type(tokens)}")
        input_ids_list = tokens["input_ids"]
        attention_mask_list = tokens["attention_mask"]

        split_with_chunksize = lambda x: np.split(x,np.arange(chunk_size,len(x),(chunk_size-2)))
        pad_with_chunksize_input_vec = lambda x: np.pad(x,(0,(chunk_size-x.size)),"constant",constant_values=(self.tokenizer.eos_token_id)) if x.size<chunk_size else x
        pad_with_chunksize_attention_vec = lambda x: np.pad(x,(0,(chunk_size-x.size)),"constant",constant_values=(0)) if x.size<chunk_size else x

        if len(input_ids_list.squeeze(0)) > chunk_size:
            input_ids_list = split_with_chunksize(input_ids_list.squeeze(0))
            attention_mask_list = split_with_chunksize(attention_mask_list.squeeze(0))
        input_ids_list = np.array(list(map(pad_with_chunksize_input_vec,input_ids_list)),np.int32)
        attention_mask_list = np.array(list(map(pad_with_chunksize_attention_vec,attention_mask_list)),np.int32)

        tokens = {}
        tokens["input_ids"] = input_ids_list
        tokens["attention_mask"] = attention_mask_list

        return tokens

    def decode_text(self,tokens):
        text_list = []
        for index in range(len(tokens)):
            raw_text = self.tokenizer.decode(tokens[index],skip_special_tokens=True)
            text = raw_text.split("generate:")[-1]
            text_list.append(text)
        processed_text: str = " ".join(text_list)
        return processed_text

    # Doesn't accept list
    def generate_text(self,tokens,early_stopping=False):
        value: np.ndarray = self.model.generate(
            input_ids=tokens["input_ids"],
            attention_mask=tokens["attention_mask"],
            min_length=10, # Used by Greedy  and Beam Search
            # max_new_tokens=self.model_config["max_new_tokens"], # Used by Beam
            max_length=self.model_config["max_length"], # Used by Greedy
            early_stopping=True, # Defaulting True leads to working in Greedy 
            num_beams=self.model_config["num_beams"], # Defaults 1 for Greedy
            do_sample=self.model_config["do_sample"], # Enabling results in Beam Search while Greedy for False
            # num_beam_groups=self.model_config["num_beam_groups"], #Can make issues
            no_repeat_ngram_size=self.model_config["no_repeat_ngram_size"], # Used by both
            length_penalty=self.model_config["length_penalty"], # Used by both
            temperature=self.model_config["temperature"], # Used by both
            num_return_sequences=1,
        ).numpy()
        tmp_tokens = tokens["input_ids"].squeeze(0)
        tmp_value: np.ndarray = value.squeeze(0)
        print(f"[no of tokens to remove]:{len(tmp_tokens)}")
        for _iter in range(len(tmp_tokens)):
            tmp_value = np.delete(tmp_value,0)
        value = tmp_value
        return [value]

    def generate_story(self,text,loop_count=1):
        suffix = "write a story"
        text = " ".join([text,suffix])

        token_list = []
        encoded_tokens = self.encode_text(text,400)
        print(f"[encoded_tokens]: {encoded_tokens}")
        print(f"[input_ids]: {encoded_tokens['input_ids']}")
        print(f"[len(input_ids)]: {len(encoded_tokens['input_ids'])}")
        print(f"[len(input_ids_item)]: {len(encoded_tokens['input_ids'][0])}")

        for _iter in range(loop_count):
            generated_tokens: list = self.generate_text(encoded_tokens)
            print(f"[generated_tokens]: {generated_tokens}")
            token_list.append(generated_tokens[0])

            imp_input_ids = self.get_imp_tokens(generated_tokens)
            imp_attention_mask = self.generate_attention_mask(generated_tokens)
            encoded_tokens = {
                "input_ids": imp_input_ids,
                "attention_mask" : imp_attention_mask
            }
        tokens = np.concatenate(token_list,axis=0)
        decoded_text = self.decode_text(tokens)
        decoded_text = decoded_text.replace("<|endoftext|>","")
        return decoded_text


if __name__ == "__main__":
    para = """
        On January 15, 2001, Jimmy Wales and Larry Sanger launched Wikipedia. Sanger coined its name as a blend of "wiki" and "encyclopedia".
        Wales was influenced by the "spontaneous order" ideas associated with Friedrich Hayek and the Austrian School of economics after being exposed to these ideas by Austrian economist and Mises Institute Senior Fellow Mark Thornton.
        Initially available only in English, versions in other languages were quickly developed.
        Its combined editions comprise more than 59 million articles, attracting around 2 billion unique device visits per month and more than 17 million edits per month (1.9 edits per second) as of November 2020.
        In 2006, Time magazine stated that the policy of allowing anyone to edit had made Wikipedia the "biggest (and perhaps best) encyclopedia in the world".
        Wikipedia has received praise for its enablement of the democratization of knowledge, extent of coverage, unique structure, culture, and reduced degree of commercial bias; but criticism for exhibiting systemic bias, particularly gender bias against women and alleged ideological bias.
        The reliability of Wikipedia was frequently criticized in the 2000s but has improved over time, as Wikipedia has been generally praised in the late 2010s and early 2020s.
        The website's coverage of controversial topics such as American politics and major events like the COVID-19 pandemic and the Russian invasion of Ukraine has received substantial media attention.
        It has been censored by world governments, ranging from specific pages to the entire site.
        In April 2018, Facebook and YouTube announced that they would help users detect fake news by suggesting fact-checking links to related Wikipedia articles.
        Articles on breaking news are often accessed as a source of frequently updated information about those events.
        Various collaborative online encyclopedias were attempted before the start of Wikipedia, but with limited success.
        Wikipedia began as a complementary project for Nupedia, a free online English-language encyclopedia project whose articles were written by experts and reviewed under a formal process.
        It was founded on March 9, 2000, under the ownership of Bomis, a web portal company.
        Its main figures were Bomis CEO Jimmy Wales and Larry Sanger, editor-in-chief for Nupedia and later Wikipedia.
        Nupedia was initially licensed under its own Nupedia Open Content License, but even before Wikipedia was founded, Nupedia switched to the GNU Free Documentation License at the urging of Richard Stallman.
        Wales is credited with defining the goal of making a publicly editable encyclopedia, while Sanger is credited with the strategy of using a wiki to reach that goal.
        On January 10, 2001, Sanger proposed on the Nupedia mailing list to create a wiki as a "feeder" project for Nupedia.
    """
    st = Story_Module()
    # encoded_tokens = st.encode_text(para)
    # print(f"[encoded_tokens(main)]: {encoded_tokens}")
    # print(f"[input_ids(main)]: {encoded_tokens['input_ids']}")

    # imp_tokens = st.get_imp_tokens((encoded_tokens["input_ids"])[0])
    # print(f"[imp_tokens(main)]: {imp_tokens}")
    # txt = "<|endoftext|><|endoftext|><|endoftext|> Hello people [EOS]<|endoftext|> boy [EOS][EOS][EOS][EOS][EOS][EOS][EOS]"
    # print(f"[eostokenstr]: {st.tokenizer.eos_token}")
# 
    # encoded_txt = st.tokenizer.encode_plus(
        # txt,
        # add_special_tokens=False,
        # return_attention_mask=True,
        # return_tensors="np",
    # )
    # print(f"[encoded_txt(input_ids)]: {encoded_txt['input_ids']}")
    # print(f"[encoded_txt(attention_mask)]: {encoded_txt['attention_mask']}")
# 
    # attention_mask = st.generate_attention_mask(encoded_txt["input_ids"][0])
    # print(f"[attention_mask]: {attention_mask}")

    inx = "The boy was a brave man. He did "
    output = st.generate_story(inx)
    print(f"[input]:\n{inx}")
    print(f"[output]:\n{output}")