from moviepy.editor import CompositeVideoClip


class Gif:
    def __init__(self, output_uri):
        self.output_uri = output_uri

    def generate_composite_gif(self, video, text):
        compo = CompositeVideoClip([video, text])
        compo.write_gif(self.output_uri, verbose=False, logger=None)
        return None
