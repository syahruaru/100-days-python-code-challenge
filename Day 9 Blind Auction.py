from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
participant = {}
new_participant = "yes"
while new_participant == "yes":
  name = input("tuliskan nama anda: \n")
  bid = int(input("Masukan angka bid: \n$"))
  participant[name]=bid
  #print(participant[name])
  clear()
  new_participant = input("Apakah ada peserta lain?,\n tuliskan 'yes' jika ada, tulis 'no' jika tidak.\n").lower()
  if new_participant == "no":
    print(participant)
    max = max(participant, key=participant.get)
    print(f"pemenang lelang adalah: {max}! dengan bidding sebesar ${participant[max]}")


