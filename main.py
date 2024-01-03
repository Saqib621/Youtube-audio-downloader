import pytube
import os

def download_youtube_audio():
    while True:
        link = input(" enter the url you want to download youtube link: " + os.linesep + os.linesep)
        print('\n')
        video_instance=pytube.YouTube(link)
        stream=video_instance.streams.filter(only_audio=True).first()
        print('Enter the location you want to save or leave it blank for current location: ')

        try:
            destination = input('>>') or '.'
            outfile=stream.download(output_path=destination)
            base,ext = os.path.splitext(outfile)
            newfile = base + '.mp3'
            os.rename(outfile,newfile)
            print('Your file has been download in the desired folder')

        except Exception as e:
            print(f"Error: {str(e)}")
            print("File could not be downloaded.")

        finally:
            statement=str(input('To continue/start again type: y '+ os.linesep + os.linesep +  'To exit type: n' + os.linesep + os.linesep))
            if statement.lower() != 'y':
                break

if __name__ == "__main__":
    download_youtube_audio()
