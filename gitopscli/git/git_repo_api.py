from abc import ABCMeta, abstractmethod
from typing import NamedTuple, Optional


class GitRepoApi(metaclass=ABCMeta):
    class PullRequestIdAndUrl(NamedTuple):
        pr_id: int
        url: str

    @abstractmethod
    def get_username(self) -> Optional[str]:
        raise NotImplementedError

    @abstractmethod
    def get_password(self) -> Optional[str]:
        raise NotImplementedError

    @abstractmethod
    def get_clone_url(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def create_pull_request(
        self, from_branch: str, to_branch: str, title: str, description: str
    ) -> "PullRequestIdAndUrl":
        raise NotImplementedError

    @abstractmethod
    def merge_pull_request(self, pr_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_pull_request_comment(self, pr_id: int, text: str, parent_id: Optional[int] = None) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_branch(self, branch: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_branch_head_hash(self, branch: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_pull_request_branch(self, pr_id: int) -> str:
        raise NotImplementedError