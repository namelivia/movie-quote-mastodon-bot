from .bot import Bot
from .subs import Subs
from .text_clip import TextClip
from .video_clip import VideoClip
from .mastodon import MastodonAPI
from .gif import Gif


class Factory:
    def __init__(self, config):
        self.config = config

    def build(self):
        subs = Subs(self.config.get("subs_uri"), self.config.get("subs_encoding"))
        text_clip = TextClip(
            self.config.get("text_size"),
            self.config.get("text_color"),
            self.config.get("text_font"),
        )
        video_clip = VideoClip(self.config.get("video_uri"))
        mastodon = MastodonAPI(
            self.config.get("mastodon_enabled"),
            self.config.get("mastodon_client_id"),
            self.config.get("mastodon_client_secret"),
            self.config.get("mastodon_api_base_url"),
            self.config.get("mastodon_login"),
            self.config.get("mastodon_password"),
            self.config.get("output_uri"),
        )
        gif = Gif(self.config.get("output_uri"))
        return Bot(subs, text_clip, video_clip, mastodon, gif)
