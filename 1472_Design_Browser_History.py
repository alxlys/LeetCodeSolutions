# https://leetcode.com/problems/design-browser-history/
class Node:
    def __init__(self, val, _next, prev):
        self.val = val
        self.next = _next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):

    def visit(self, url: str) -> None:

    def back(self, steps: int) -> str:

    def forward(self, steps: int) -> str:
        pass


if __name__ == '__main__':
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")  # You are in "leetcode.com".Visit "google.com"
    browserHistory.visit("facebook.com")  # You are in "google.com".Visit "facebook.com"
    browserHistory.visit("youtube.com")  # You are in "facebook.com".Visit "youtube.com"
    browserHistory.back(1)  # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    browserHistory.back(1)  # You are in "facebook.com", move back to "google.com" return "google.com"
    browserHistory.forward(1)  # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    browserHistory.visit("linkedin.com")  # You are in "facebook.com".Visit "linkedin.com"
    browserHistory.forward(2)  # You are in "linkedin.com", you cannot move forward any steps.
    browserHistory.back(
        2)  # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    browserHistory.back(
        7)  # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
