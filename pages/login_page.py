from abc import abstractmethod, ABCMeta


class LoginPage(metaclass=ABCMeta):

    @abstractmethod
    def enter_username(self, username): raise NotImplementedError

    @abstractmethod
    def enter_password(self, password): raise NotImplementedError

    @abstractmethod
    def press_login_button(self): raise NotImplementedError

    @abstractmethod
    def check_error_message(self, error_message): raise NotImplementedError

    @abstractmethod
    def check_page_title(self, page_title): raise NotImplementedError

    @abstractmethod
    def check_login_button_disabled(self): raise NotImplementedError
