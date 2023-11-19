from youtube_transcript_api import YouTubeTranscriptApi
import json

class Youtube:
    def __init__(self,  text=None, start=None):
        self.text = text
        self.start = start
    def to_json(self):
        return {
            "start": self.start,
            "text": self.text
        }
    
    def get_transcript(self, video_id):
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        map_transcript = [Youtube(entry['text'], entry['start']) for entry in transcript]

        return json.dumps([transcript.to_json() for transcript in map_transcript])