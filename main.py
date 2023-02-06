text = """ 
Champagne ring bells in the streets of Jamaica
Started at the crib, look how far this shit/l take ya
Ross sittin on 235 acres (I been tryin, tryin, tryin, tryin)

And that/s facts, Hamdan Mohammed like my third cousin (facts)
Mansoor Mohammed like my real brother (facts)
Dubai embrace me like a Emirati (facts)
All my Rolls Royces got a different body (facts)
Mansory, kitted out with every option (facts)
Lemme know if that/s a problem (I been tryin, tryin, tryin, tryin)

If you got a problem with me, gotta walk around it
Used to say I had fore I got it, now I got it all
And bein honest, I don/t really wanna talk about it
And if I didn/t have it, wouldn/t wanna sulk about it
(I been tryin, tryin, tryin,  tryin)

I had it so long, I don/t even celebrate it
Negative thoughts don/t even enter my inner matrix
Magine me still rappin bout if I never made it
(I been tryin, tryin, tryin, trying)

Damn, not too many parallels left in our lives
I mean, my crib look bigger through my son/s eyes
And the squad look bigger to the young guys
"""


print(len(text.split()))

word_count = {}
for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1  
  else:
    word_count[word] = 1
  print(word_count)