see how to install.png for installation

Using open source package OpenALPR for plate recognition. https://github.com/openalpr/openalpr
Poor package installation for OpenALPR package -> had to put all the codes in this folder
images, videos and outputs are all in samples folder

run image_recognition.py to recognistion numberplate from a single image
run video_recognition.py to recognistion numberplates from a video
Very fast process - almost real time
Performance on par with human performance. But if quality of video is poor where human eye struggle to recognise the plate number, model appears to be useless.
output all number plates detected to samples/plate_no.csv to get ready for making API calls to check MOT in R.

Run API_call.R in R studio to retrieve information based on number plate predictions
returns out.csv in samples folder with information on valid registration numbers, car model and past MOT test results
There are inconsistencies in the format of API call results depending on the vechicle condition. But code should be easy to manipulate to capture desired information.

Key to move forward:
- improve quality of video. Consider neighbouring images as a group and superimpose them in a way so we can reconstruct fragmented information
- Super Resolution networks seem to be way too slow and useless out of the box for now. But it should perform much better if we can supply loads of high resolution images to 
train the network
- build our own numberplate neural network and make it perform more predictions even at low res environment - once we get some educated guesses the API call process can 
help us filter out any false predictions.