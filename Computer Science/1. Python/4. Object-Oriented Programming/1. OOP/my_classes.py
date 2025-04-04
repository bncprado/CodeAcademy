class Musician:
  def __init__(self, input_name, input_instrument, input_band, input_gets_paid=False, input_payment=0):
    self.name = input_name
    self.instrument = input_instrument
    self.band = input_band
    self.gets_paid = input_gets_paid
    self.payment = input_payment


  def gig_payment(self,gig_payment):
    self.payment = self.payment + gig_payment
    print(f"{self.name} got paid ${gig_payment:.2f}. He made ${self.payment:.2f} playing with {self.band}")

gnr_vocal = Musician("Axl", "Singer", "Guns N' Roses")
gnr_lead_guitar = Musician("Slash", "Guitar", "Guns N' Roses", False)
