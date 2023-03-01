import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = '1'

from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
import tensorflow as tf
import numpy as np


class Summary_Module:
    def __init__(self):
        self.load_model_config()
        self.load_tokenizer()
        self.load_model()

    def load_model_config(self):
        self.model_config = {}
        self.model_config["do_sample"] = None
        self.model_config["num_beams"] = 1
        self.model_config["num_beam_groups"] = 2
        self.model_config["max_new_tokens"] = 1024
        self.model_config["max_length"] = 1024
        self.model_config["no_repeat_ngram_size"] = 2
        self.model_config["length_penalty"] = 1.
        self.model_config["temperature"] = 1.

    def load_tokenizer(self):
        self.tokenizer: GPT2Tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def load_model(self):
        self.model: TFGPT2LMHeadModel = TFGPT2LMHeadModel.from_pretrained("gpt2")

    def unload_tokenizer(self):
        del self.tokenizer
        self.tokenizer = None

    def unload_model(self):
        del self.model
        self.model = None

    def encode_text(self,text,chunk_size=600):
        tokens = self.tokenizer.encode_plus(
            text,
            add_special_tokens=False,
            return_attention_mask=True,
            return_token_type_ids=False,
            return_tensors="np",
        )
        raw_input_ids_list = tokens["input_ids"]
        raw_attention_mask_list = tokens["attention_mask"]

        # split_with_chunksize = lambda x: np.split(x,np.arange(chunk_size,len(x),(chunk_size-2)))
        # pad_with_chunksize_input_vec = lambda x: np.pad(x,(0,(chunk_size-x.size)),"constant",constant_values=(self.tokenizer.eos_token_id)) if x.size<chunk_size else x
        # pad_with_chunksize_attention_vec = lambda x: np.pad(x,(0,(chunk_size-x.size)),"constant",constant_values=(0)) if x.size<chunk_size else x

        # input_ids_list = split_with_chunksize(raw_input_ids_list[0])
        # attention_mask_list = split_with_chunksize(raw_attention_mask_list[0])
        # input_ids_list = np.array(list(map(pad_with_chunksize_input_vec,input_ids_list)))
        # attention_mask_list = np.array(list(map(pad_with_chunksize_attention_vec,attention_mask_list)))

        # print(input_ids_list)
        # tokens = {}
        # tokens["input_ids"] = input_ids_list
        # tokens["attention_mask"] = attention_mask_list
        input_ids_list = raw_input_ids_list
        attention_mask_list = raw_attention_mask_list
        split_with_chunksize = lambda x: np.split(x,np.arange(chunk_size,len(x),(chunk_size-2)))
        pad_with_chunksize_input_vec = lambda x: np.pad(x,(0,(chunk_size-x.size)),"constant",constant_values=(self.tokenizer.eos_token_id)) if x.size<chunk_size else x
        pad_with_chunksize_input_vec = lambda x: np.pad(x,(0,(chunk_size-x.size)),"constant",constant_values=(self.tokenizer.eos_token_id)) if x.size<chunk_size else x
        pad_with_chunksize_attention_vec = lambda x: np.pad(x,(0,(chunk_size-x.size)),"constant",constant_values=(0)) if x.size<chunk_size else x

        if len(input_ids_list.squeeze(0)) > chunk_size:
            input_ids_list = split_with_chunksize(input_ids_list.squeeze(0))
            attention_mask_list = split_with_chunksize(attention_mask_list.squeeze(0))
        input_ids_list = np.array(list(map(pad_with_chunksize_input_vec,input_ids_list)),np.int32)
        attention_mask_list = np.array(list(map(pad_with_chunksize_attention_vec,attention_mask_list)),np.int32)

        # paddings = []
        # for item in 
 
        tokens = {}
        tokens["input_ids"] = input_ids_list
        tokens["attention_mask"] = attention_mask_list
        # tokens["pad_size"] = (chunk_size-x.size)

        return tokens

    def decode_text(self,tokens):
        text_list = []
        # processed_text = self.tokenizer.decode(tokens,skip_special_tokens=True)
        for index in range(len(tokens)):
            raw_text = self.tokenizer.decode(tokens[index],skip_special_tokens=True)
            # text = raw_text.split("TL;DR:")[-1]
            text_list.append(raw_text)
        # processed_text: str = " ".join(text_list)
        # return processed_text
        return text_list

    def generate_text(self,tokens):
        value: np.ndarray = self.model.generate(
            input_ids=tokens["input_ids"],
            attention_mask=tokens["attention_mask"],
            min_length=30, # Used by Greedy  and Beam Search
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
        # tmp_tokens = tokens["input_ids"]
        # tmp_value = None
        # final_result = []
        # for entity in tmp_tokens:
            # tmp_value = entity
            # print(f"[no of tokens to remove]:{len(entity)}")
            # for _iter in range(len(entity)-2):
                # tmp_value = np.delete(tmp_value,0)
            # final_result.append(tmp_value) 
        # return final_result
        return value

    def generate_summary(self,text):
        suffix = "TL;DR:"
        text = " ".join([text,suffix])

        encoded_tokens = self.encode_text(text,600)
        generated_tokens = self.generate_text(encoded_tokens)
        decoded_text = self.decode_text(generated_tokens)
        # decoded_text = decoded_text.replace("<|endoftext|>","")
        # print(f"[decoded_text]: {decoded_text}")
        # for index in range(len(decoded_text)):
            # if decoded_text[index].find("TL;DR:") != -1:
                # decoded_text[index] = None
                # continue
            # decoded_text[index] = decoded_text[index].split("TL;DR:")[-1]
        # decoded_text = list(filter(None,decoded_text))

        print(f"[len(decoded_text)]: {len(decoded_text)}")
        for line in decoded_text:
            print(f"[text]: {line}")

        decoded_text = "".join(decoded_text)
        return decoded_text

if __name__ == "__main__":
    sm = Summary_Module()
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

    sm.generate_summary(para)