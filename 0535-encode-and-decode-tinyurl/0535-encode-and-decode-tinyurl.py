class Codec:
    def __init__(self):
        self.url = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url:
            return "http://tinyurl.com/" + url[longUrl]
        else:
            code = str(len(self.url) + random.randint(0, 10000))
            short = "http://tinyurl.com/" + code
            self.url[short] = longUrl
            return short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))