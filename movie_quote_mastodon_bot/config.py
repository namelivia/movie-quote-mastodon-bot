class Config:
    def _is_true(self, value):
        return value.lower() == "true"

    def __init__(self, source):
        self.config = {
            "idle_period": int(source["IDLE_PERIOD"]),
            "subs_uri": source["SUBS_URI"],
            "subs_encoding": source["SUBS_ENCODING"],
            "video_uri": source["VIDEO_URI"],
            "output_uri": source["OUTPUT_URI"],
            "mastodon_enabled": self._is_true(source["MASTODON_ENABLED"]),
            "mastodon_client_id": source["MASTODON_CLIENT_ID"],
            "mastodon_client_secret": source["MASTODON_CLIENT_SECRET"],
            "mastodon_api_base_url": source["MASTODON_API_BASE_URL"],
            "mastodon_login": source["MASTODON_LOGIN"],
            "mastodon_password": source["MASTODON_PASSWORD"],
            "text_size": int(source["TEXT_SIZE"]),
            "text_color": source["TEXT_COLOR"],
            "text_font": source["TEXT_FONT"],
        }

    def get(self, key):
        return self.config[key]
