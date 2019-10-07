Questions  
Describe your solution in detail. What neural network did you use? What dataset was it trained on? What accuracy does it achieve?  

>> Used the dilib for Face Recognition. The model has an accuracy of 99.38% on the Labeled Faces in the Wild benchmark. It uses the ResNet network with 29 conv layers. 

Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?

>> The results are reasonably accurate and it could be used for a robust production-grade system, depending on the application.

What framerate does this method achieve on the Jetson? Where is the bottleneck?

>> There is no delay in image production and seems much faster than opencv. 

Which is a better quality detector: the OpenCV or yours?

>> dilib is better quality.

References:  
http://blog.dlib.net/2017/02/high-quality-face-recognition-with-deep.html  
https://github.com/ageitgey/face_recognition  
