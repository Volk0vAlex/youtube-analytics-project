from src.channel import Channel


class Video(Channel):

    def __init__(self, video_id: str):

        self.youtube = Channel.get_service()
        self.video_id = video_id

        try:
            self.video = self.youtube.videos().list(part='snippet, statistics, contentDetails, topicDetails',
                                                    id=video_id
                                                    ).execute()

            self.video_title: str = self.video["items"][0]["snippet"]["title"]
            self.video_url = f"https://www.youtube.com/watch?v={self.video_id}"
            self.view_count: int = self.video["items"][0]["statistics"]["viewCount"]
            self.like_count: int = self.video["items"][0]["statistics"]["likeCount"]

        except Exception:
            self.video_title = None
            self.video_url = None
            self.view_count = None
            self.like_count = None



    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        self.playlist_id = playlist_id
        super().__init__(video_id)
