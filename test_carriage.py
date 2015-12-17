from HeadHorizontalCarriage import HeadHorizontalCarriage

c = HeadHorizontalCarriage()

while True:
  cmd = str(raw_input("Next"))
  if cmd=="exit":
    break
  c.goToNextPosition()
