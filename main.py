from youtube import Youtube
from generative_ai import GenerativeAI
import argparse
import socketserver
import routes
# Specify the port you want to use
PORT = 8001
        
def main():
    parser = argparse.ArgumentParser(description="Youtube Chapterizer",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--video", type=str, help="youtube video to be paste e.g https://www.youtube.com/watch?v=xxxxxxxx")
    parser.add_argument("-n", "--chapters", type=str, help="request amount of chapters")
    parser.add_argument("-s", "--web-server", type=bool, help="activate web-server", default=False)
    args = parser.parse_args()
    config = vars(args)

    if config["web_server"]:
        # Create the server
        with socketserver.TCPServer(("", PORT), routes.ChapterGenerator) as httpd:
            print("Serving at port", PORT)
            httpd.serve_forever()
    else:
        if config["video"] is None:
            print("no value was provided")
            exit()
        else:
            video_id = config["video"].split("=")

            transcript = Youtube().get_transcript(video_id[1])

            response = GenerativeAI().interact(prompt=transcript)
                    
            # print(response)

main()