Questions:

**Part 1**  
In the time allowed, how many images did you annotate?  
> ~ 300 images were annotated

Home many instances of the Millennium Falcon did you annotate? How many TIE Fighters?  
> ~ roughly about half of each

Based on this experience, how would you handle the annotation of large image data set?  
> Crowdsourcing, or build it into a product so customers would annotate for me.

Think about image augmentation? How would augmentations such as flip, rotation, scale, cropping, and translation effect the annotations?  
> scale, flip and translate would be 'easier' with less that could go wrong. Rotation would change the size of the image, which could be a problem. Cropping would have the same size challenges as well as missing information

**Part 2**  
Describe the following augmentations in your own words:  
> Flip:  the image is inverted where left becomes right (vertical flip)  

> Rotation:  The image rotate on its middle axis, which increases the size of the overall image; thus changing the shape.  

> Scale:  the number of pixels changes (shrinks or expands) which changes how well image detection works.  

> Crop:  pixel loss, where only the pixels you care about are used -- could potentially lose valuable information.  

> Translation: white space is added to th corners of an image. 

> Noise:  adding blurring, random pixels; thus making it harder to read the image.

**Part 3**  
Image annotations require the coordinates of the objects and their classes; in your option, what is needed for an audio annotation?
> In audio annotation time matters; the gaps between words, the length of words as well as their meaning.  
