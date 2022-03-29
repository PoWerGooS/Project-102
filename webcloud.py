import cv2
import dropbox
import time
import random

starttime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result= True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName='image'+str(number)+'.png'
        cv2.imwrite(imageName,frame)
        starttime=time.time
        result = False
    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()

        

def uploadFile(imageName):
    access_token = 'sl.BEq8o6cc4LMG5shkZwN0BTsAtBXwEGhX8JKtve3iCcHItYcQ881ja67K8f1sNdPiXeuWIwaUzcrmTotE6j9AiRmfpuCq-5QDvmLLp2TyiqoiA8onTH4PwTLW_Y_p95ERpk2eTOZL4gyV'
    file=imageName
    file_from = file
    file_to = '/testFolder/'+(imageName)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
def main(): 
    while(True): 
        if ((time.time() - starttime) >= 5):
            name = takeSnapshot() 
            uploadFile(name)
main()