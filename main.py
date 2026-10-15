from maps.GakushokuSample import GakushokuSample

data = [GakushokuSample(), ]

for rank, d in enumerate(data, start=1):
	print(f"{rank}位: {d.get_menu()}")
	print(f"---------------------------------")
	print(d.get_summary())
	print(d.get_author())
	print()