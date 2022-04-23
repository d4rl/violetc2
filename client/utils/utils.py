from colored import fg, bg, attr

class Print:
	def good(text:str) -> None:
		print(f"{fg(15)}[{fg(21)}+{fg(15)}] {text}")

	def bad(text:str) -> None:
		print(f"{fg(15)}[{fg(196)}+{fg(15)}] {text}")

class Returns:
	def good(text:str) -> str:
		return f"{fg(15)}[{fg(21)}+{fg(15)}] {text}"

	def bad(text:str) -> None:
		return f"{fg(15)}[{fg(196)}+{fg(15)}] {text}"

