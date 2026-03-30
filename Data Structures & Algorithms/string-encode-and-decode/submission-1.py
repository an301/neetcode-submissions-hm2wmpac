class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for char in strs:
            output += char + "+SPACE+"
        print(output)
        return output

    'neet+code+love+you+'

    def decode(self, s: str) -> List[str]:
        output = s.split('+SPACE+')
        output.pop()
        return output