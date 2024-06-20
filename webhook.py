from typing import Any, Dict, Self
import os
import requests
import time

class EmbedBuilder:
    def __init__(self) -> None:
        self.data = {
            'color': "",
            'author': {},
            'title': "",
            'url': "",
            'description': "",
            'fields': [],
            'image':  {},
            'thumbnail':  {},
            'footer':  {},
            'timestamp': "",
        }

    def setColor(self, color: str) -> Self:  # Discord uses decimal numeral system for colors not hex
        self.data['color'] = color
        return self

    def setAuthor(self, name: str = "", url: str = "", icon_url: str = "") -> Self:
        self.data['author'] = {
            "name": name or "",
            "url": url or "",
            "icon_url": icon_url or "",
		}
        return self

    def setTitle(self, title: str) -> Self:
        self.data['title'] = title
        return self

    def setUrl(self, url: str) -> Self:
        self.data['url'] = url
        return self

    def setDescription(self, description: str) -> Self:
        if len(description) >= 2000:
            raise Exception("Description cannot contain more than 2000 characters")
        self.data['description'] = description
        return self

    def addField(self, name: str = "", value: str = "", inline: bool = False) -> Self:
        self.data['fields'].append({'name': name, 'value': value, 'inline': inline})
        return self

    def setImage(self, imageUrl: str) -> Self:
        self.data['image'] = {'url': imageUrl}
        return self

    def setThumbnail(self, thumbnailUrl: str) -> Self:
        self.data['thumbnail'] = {'url': thumbnailUrl}
        return self

    def setFooter(self, text: str = "", iconUrl: str = "") -> Self:
        self.data['footer'] = {'text': text, 'icon_url': iconUrl}
        return self

    def setTimestamp(self, timestamp: str) -> Self: 
        """
        Format: "2015-12-31T12:00:00.000Z"
        """
        self.data['timestamp'] = timestamp
        return self

    def getFiltered(self) -> Dict[str, Any]:
        return {k: v for k, v in self.data.items() if v}
            
class DiscordWebhook:
    def __init__(self, url: str, content: str = "", username: str = "", avatarUrl: str = "", tts: bool = False) -> None:
        self.url = url
        self.files = {}
        self.data = {
            'embeds': [],
            'content': content,
            'username': username,
            'avatarUrl': avatarUrl,
            'tts': tts
        }
	
    def addFile(self, filePath: str, fileName: str = "") -> None:
        def getNameFromPath(filePath: str) -> str:
          return os.path.basename(filePath)
        """
        Args: 
            filePath (str): The relative or absolute path of the file to be added
        """
        try:
            f = open(filePath, "rb")
            out = f.read()
            f.close()
            if(not fileName): fileName = getNameFromPath(filePath) # Use the files name if there is no override
            self.files[fileName] = out
        except Exception as e:
            print(f"Request failed: {e}")

    def clearEmbeds(self) -> None:
        self.data['embeds'] = []

    def addEmbed(self, embed: EmbedBuilder) -> None:
        if(len(self.data['embeds']) == 10): raise Exception("Cannot add more than 10 embeds to a request")
        self.data['embeds'].append(embed.getFiltered())
        
    def setContent(self, content: str) -> None:
        self.data['content'] = content

    def setUsername(self, username: str) -> None:
        self.data['username'] = username

    def setAvatarUrl(self, avatarUrl: str) -> None:
        self.data['avatarUrl'] = avatarUrl
    
    def setTts(self, tts: bool) -> None:
        self.data['tts'] = tts
        
    def getFiltered(self) -> Dict[str, Any]: # Returns data after filtering for empty values
        return {k: v for k, v in self.data.items() if v}
    
    def execute(self, max_retries=5) -> bool:
        """
        Returns:
            204 for success
            429 for rate limit
        """
        if not self.data['embeds'] and not self.data['content'] and not self.files:
            raise Exception("Request requires a content, embed or file field")
    
        retries = 0
        while retries < max_retries:
            try:
                res = requests.post(self.url, json=self.getFiltered(), files=self.files)
                res.raise_for_status()
                if res.status_code != 429:
                    return res.status_code # Return on success
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
            if res.status_code == 429:
                retries += 1
                print(f"Rate limit reached, retrying request after waiting {2*retries} seconds")
                time.sleep(2 * retries)  # Wait for a second before retrying
        return res.status_code
            
