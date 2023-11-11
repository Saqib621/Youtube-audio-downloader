import pytube
import os
statement='y' 
while statement == 'y' :
    link = str(input(" enter the url you want to download youtube link " + os.linesep + os.linesep))
    print('\n')
    video_instance=pytube.YouTube(link)
    stream=video_instance.streams.filter(only_audio=True).first()
    print('Enter the location you want to save or leave it blank for current location')

    try:
        destination = str(input('>>')) or '.'
        outfile=stream.download(output_path=destination)
        base,ext = os.path.splitext(outfile)
        newfile = base + '.mp3'
        os.rename(outfile,newfile)
        print('Your file has been download in the desired folder')
        
        
    except:
        print("File is already download in the current folder")

    finally:
        statement=str(input('for continue type : y '+ os.linesep + os.linesep +  'for exit type :n' + os.linesep + os.linesep))



