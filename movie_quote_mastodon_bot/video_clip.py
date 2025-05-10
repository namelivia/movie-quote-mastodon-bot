from moviepy.editor import VideoFileClip


class VideoClip:
    def __init__(self, video_uri):
        self.video_uri = video_uri

    def generate_quote_video(self, quote):
        return (
            VideoFileClip(self.video_uri)
            .subclip(str(quote.start), str(quote.end))
            .resize(0.3)
        )
