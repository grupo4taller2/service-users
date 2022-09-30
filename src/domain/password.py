from src.domain.password_encoder import PasswordEncoder


class Password:
    def __init__(self, encoder: PasswordEncoder, plain_text: str):
        self.hashed_password = encoder.encode(plain_text)
