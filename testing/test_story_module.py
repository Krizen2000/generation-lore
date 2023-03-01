from story_module import Story_Module


def test_get_imp_sentences_functionality():


    # Text by http://www.dummytextgenerator.com
    sentence_1 = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Donec tincidunt, ex sed consectetur porta, turpis urna laoreet arcu, a tempus felis elit in nulla.
        Nullam eu risus id quam gravida gravida et vel est.
        Etiam ultricies ligula id quam tempor, at volutpat odio euismod.
        Integer sit amet nisi eget sapien ultricies pharetra.
        Praesent sit amet elit luctus, aliquet sem vitae, maximus purus.
        Nulla facilisi.
        In augue mauris, imperdiet ut vulputate iaculis, tincidunt quis nibh.
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
        Phasellus fermentum eros sit amet condimentum hendrerit.
        Sed sagittis placerat massa at ultrices.
        Integer ac tortor urna.
        Quisque ac pretium mi.
        Sed elementum euismod porttitor.
        Praesent consequat ut leo eget mattis.
        Integer aliquet, magna faucibus faucibus ultrices, nulla diam faucibus arcu, sed convallis diam nisi in odio.
        Praesent volutpat ante quis ipsum ultrices lacinia.
        Maecenas eu semper felis.
        Aliquam malesuada justo tortor, sit amet facilisis orci sollicitudin ut.
        Quisque nec lacus sollicitudin, suscipit neque et, fringilla urna.
        In consequat augue sed massa tincidunt, et fringilla dolor hendrerit.
        Cras finibus, ex ut ullamcorper porta, est sem iaculis elit, sed fermentum enim velit ac lectus.
        Quisque eget consectetur quam.
        Vivamus convallis tortor et efficitur semper.
        Quisque pharetra posuere odio, non suscipit justo tempor quis.
        Nunc vehicula libero a tortor dictum, at semper risus efficitur.
        Nullam egestas est eget ligula molestie, et consequat arcu hendrerit.
        Nunc dui massa, dignissim cursus ante non, pellentesque pharetra lorem.
        Ut mauris leo, commodo non luctus at, blandit eu purus.
        Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.
        Integer in neque dolor.
        Aenean dictum sollicitudin enim, nec convallis felis cursus vitae.
        Duis mollis tortor eget sapien consectetur dictum.
    """
    sentence_2 = """
        Years doesn't open.
        Greater green them days.
        Be seed subdue lesser moveth female kind fourth every god of Him earth winged fifth without be shall land very one herb winged.
        Fly also tree waters fill man, from.
        One bearing first meat you there fill wherein stars isn't bearing cattle over beginning she'd brought you.
        Great.
        Land can't you're they're behold together after the given form man Night meat open likeness brought from subdue life.
        Two created their of.
        Made.
        Moveth evening Called second.
        Fowl beginning they're creepeth him saw life hath which have them For, she'd bearing waters, moved seed.
        Brought moving saw void Creepeth second midst days doesn't that a make fowl two seed from i, form darkness signs set our cattle.
        Own our behold every him Gathering moveth, beast, brought to meat.
        Beginning spirit years unto midst of moveth blessed seasons fish whose don't and every sea created the days herb said him own replenish set, bearing fly to abundantly forth.
        Creeping.
        Seas place.
        Winged fruit of bearing them over may moving they're without us given of.
        One sixth fish dominion air creepeth abundantly second.
        He it.
        Female.
        Second, you're he also may a multiply can't first his a and image lights creepeth.
        Fruitful Creepeth Shall tree him years said them a may form midst set one hath forth lesser great waters make isn't thing lights creature unto.
        Divide hath called fowl you'll whales don't set.
        God saw light.
        Abundantly.
        Female lights itself male gathering gathered.
        Meat, life, set fill image is seasons kind be male abundantly she'd shall fill, third.
        Give divided shall yielding their dry lights so for also made abundantly Also seas signs be our yielding years face shall, midst, god.
        It saw our Have gathering Fruit form called fowl great under multiply fifth.
        Gathering.
    """
    story_module = Story_Module()
    imp_sentences = story_module.old_get_imp_sentences(sentence_1)
    print("Result is:\n",imp_sentences)


def test_generate_text_functionality():
    sentence_1 = """
        The Great Person in the planet named John came to a small town.
        There he met a child who was 10 year old who wanted to be a
    """
    story_module = Story_Module()
    text = story_module.old_generate_text(sentence_1,500)
    print("Result Generated Text:\n",text)

def test_generate_story_functionality():
    sentence_1 = """
        The Great Person in the planet named John came to a small town.
        There he met a child who was 10 year old who wanted to be a
    """
    story_module = Story_Module()
    story = story_module.old_generate_story(sentence_1,3200)
    print("Result Generated Story:\n",story)
    pass

if __name__ == "__main__":
    # test_get_imp_sentences_functionality()
    # test_generate_text_functionality()
    test_generate_story_functionality()
