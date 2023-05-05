# https://leetcode.com/problems/design-browser-history/
class Node:
    def __init__(self, val, _next, prev):
        self.val = val
        self.next = _next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage, None, None)

    def visit(self, url: str) -> None:
        node = Node(url, None, self.current)
        self.current.next = node
        self.current = node

    def back(self, steps: int) -> str:
        idx = 0
        while idx != steps:
            if not self.current.prev:
                break
            self.current = self.current.prev
            idx += 1
        return self.current.val

    def forward(self, steps: int) -> str:
        idx = 0
        while idx != steps:
            if not self.current.next:
                break
            self.current = self.current.next
            idx += 1
        return self.current.val


if __name__ == '__main__':
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")  # You are in "leetcode.com".Visit "google.com"
    browserHistory.visit("facebook.com")  # You are in "google.com".Visit "facebook.com"
    browserHistory.visit("youtube.com")  # You are in "facebook.com".Visit "youtube.com"
    print(browserHistory.back(1))  # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    print(browserHistory.back(1))  # You are in "facebook.com", move back to "google.com" return "google.com"
    print(browserHistory.forward(1))  # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    browserHistory.visit("linkedin.com")  # You are in "facebook.com".Visit "linkedin.com"
    print(browserHistory.forward(2))  # You are in "linkedin.com", you cannot move forward any steps.
    print(browserHistory.back(
        2))  # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    print(browserHistory.back(
        7))  # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
