from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):
	def get_menu(self):
		return "焼きそば"

	def get_summary(self):
		return "ソースが絡んで美味しい"

	def get_author(self):
		return "tmk"