from genlore.modules.story_module.story_module import Story_Module


def test_get_imp_sentences_functionality():
    
    sentence = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Donec tincidunt, ex sed consectetur porta, turpis urna laoreet arcu, a tempus felis elit in nulla. 
        Nullam eu risus id quam gravida gravida et vel est. Etiam ultricies ligula id quam tempor, at volutpat odio euismod. 
        Integer sit amet nisi eget sapien ultricies pharetra. 
        Praesent sit amet elit luctus, aliquet sem vitae, maximus purus. Nulla facilisi. 
        In augue mauris, imperdiet ut vulputate iaculis, tincidunt quis nibh. 
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
        Phasellus fermentum eros sit amet condimentum hendrerit. 
        Sed sagittis placerat massa at ultrices. 
        Integer ac tortor urna. Quisque ac pretium mi. 
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
    imp_sentences = Story_Module.get_imp_sentences(sentence)
    print("Result is:\n",imp_sentences)


if __name__ == "__main__":
    test_get_imp_sentences_functionality()

