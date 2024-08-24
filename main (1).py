import time
import random

phrases = [
    '01. The sun sets quietly over the horizon, painting the sky with brilliant colors',
    '02. Every moment we share together is a memory that will last a lifetime, forever cherished',
    '03. Dreams are the whispers of our souls, guiding us toward the path we were meant for',
    '04. In the heart of every challenge lies the opportunity to grow stronger and more resilient',
    '05. Love is a garden that flourishes when tended with care, patience, and understanding',
    '06. The sound of rain tapping on the window is a soothing lullaby for the soul',
    '07. With every step forward, you leave behind the fear that once held you back',
    '08. The stars above remind us that even in darkness, there is always a glimmer of hope',
    '09. True friendship is a treasure that grows richer with time, trust, and shared experiences',
    '10. The beauty of life lies in its unpredictability, the surprises that keep us on our toes',
    '11. Each day is a blank canvas, waiting for you to paint your dreams upon it',
    '12. Success is not measured by wealth, but by the happiness and fulfillment you find within',
    '13. The power of kindness can change the world, one small act at a time',
    '14. Nature beauty is a reminder of the simple pleasures that make life truly meaningful',
    '15. In the quiet moments, we find the clarity to see the path we need to take',
    '16. The journey of a thousand miles begins with a single step in the right direction',
    '17. Laughter is the music of the soul, a melody that brings joy to our hearts',
    '18. Every sunrise brings a new opportunity to start fresh and chase our dreams with vigor',
    '19. The love of family is the foundation upon which we build our lives and dreams',
    '20. Wisdom comes not from age, but from the experiences that shape our understanding of life',
    '21. The warmth of a hug can mend a heart thats been broken and bruised by time',
    '22. The ocean waves whisper secrets of the deep, mysteries that have yet to be uncovered',
    '23. Courage is the strength to keep going, even when the road ahead seems uncertain',
    '24. The bonds of friendship are forged in the fires of shared struggles and victories',
    '25. The beauty of a sunset is a reminder that every ending can be a new beginning',
    '26. Music has the power to heal wounds that words alone cannot reach or mend',
    '27. The future belongs to those who believe in the beauty of their dreams and aspirations',
    '28. Every challenge we face is an opportunity to grow stronger and more resilient in spirit',
    '29. The smile of a child is a beacon of hope in a world full of challenges',
    '30. A single act of kindness can ripple through the world, touching countless lives',
    '31. Life is a journey, not a destination, filled with twists, turns, and unexpected surprises',
    '32. The heart knows what the mind often forgets: the importance of love and connection',
    '33. The suns rays kiss the earth, bringing warmth and life to all living things',
    '34. In the quiet of the night, our deepest thoughts come to life, unspoken and true',
    '35. The sound of laughter is the best medicine, healing wounds we never knew we had',
    '36. The most precious moments in life are the ones we share with those we love',
    '37. The beauty of the world is reflected in the eyes of those who see with wonder',
    '38. Hope is the light that guides us through the darkest times, never letting us falter',
    '39. The strength of the human spirit is revealed in our ability to rise after every fall',
    '40. Every moment is a gift, an opportunity to create memories that will last a lifetime',
    '41. Love is the thread that weaves together the fabric of our lives and connections',
    '42. The winds of change bring new opportunities to those who are ready to embrace them',
    '43. The hearts desires often lead us to places we never imagined we would go',
    '44. The whispers of the trees tell stories of the past, present, and future intertwined',
    '45. A journey of discovery begins with the courage to step into the unknown and uncharted',
    '46. The suns warmth is a reminder of the light and love that surround us every day',
    '47. The dance of the leaves in the wind is natures ballet, a symphony of movement',
    '48. The power of dreams lies in their ability to inspire us to reach for the stars',
    '49. Every goodbye holds the promise of a new hello, a fresh start on the horizon',
    '50. The beauty of life is found in the little moments that make our hearts sing with joy',
    '51. The strength of love is measured not by its duration, but by the depth of its connection',
    '52. The sound of waves crashing on the shore is a reminder of life\'s constant ebb and flow',
    '53. A smile can brighten even the darkest of days, bringing warmth and light to the soul',
    '54. The power of words can uplift, inspire, and change the course of someones life forever',
    '55. In the stillness of the night, our dreams come alive, guiding us toward our destiny',
    '56. The beauty of the world is captured in the eyes of those who see with love',
    '57. The rhythm of life is a dance we all participate in, each step leading to the next',
    '58. The love we give is the legacy we leave behind, touching lives long after were gone',
    '59. The colors of a sunset are natures way of saying goodbye to the day with grace',
    '60. The bond between friends is a connection that transcends time, distance, and circumstance',
    '61. The magic of life is found in the moments that take our breath away with wonder',
    '62. The journey of life is filled with unexpected detours, each one teaching us something new',
    '63. The power of hope lies in its ability to keep us moving forward, despite the odds',
    '64. The beauty of nature is a reflection of the divine, a reminder of the greater picture',
    '65. Every step we take brings us closer to the dreams we\'ve been chasing all our lives',
    '66. The light of the moon guides us through the darkness, illuminating our path with hope',
    '67. The strength of a friendship is tested by time, but true bonds are never broken',
    '68. The sound of rain on the roof is a lullaby that soothes the soul to sleep',
    '69. The warmth of a smile can melt even the coldest of hearts, bringing joy and light',
    '70. The beauty of life is in the moments that make us feel alive, truly alive',
    '71. The suns rays bring warmth to the earth, nurturing life in all its forms',
    '72. The whispers of the wind carry stories of old, tales of love, loss, and triumph',
    '73. The journey of love is a path filled with twists, turns, and unexpected surprises',
    '74. The beauty of a flower is a reminder of the simple pleasures that life offers us',
    '75. The power of a hug can heal wounds that words alone cannot touch or mend',
    '76. The light of the stars reminds us that we are never truly alone in the universe',
    '77. The warmth of a fire brings comfort on a cold night, a symbol of safety and home',
    '78. The beauty of the ocean is in its vastness, a reminder of the infinite possibilities in life',
    '79. The journey of self-discovery is a path that leads us to our true purpose and destiny',
    '80. The sound of laughter is a melody that brings joy and happiness to the soul',
    '81. The power of love is in its ability to transform lives and heal broken hearts',
    '82. The beauty of a sunrise is a reminder that every day is a new beginning',
    '83. The strength of the human spirit is revealed in our ability to overcome adversity',
    '84. The warmth of the sun on our skin is a reminder of the light within us all',
    '85. The whispers of the night carry the dreams we dare not speak aloud, yet long for',
    '86. The journey of life is a tapestry woven with moments of joy, sorrow, and everything between',
    '87. The beauty of a smile is in its ability to brighten even the darkest of days',
    '88. The power of hope is in its ability to keep us moving forward, even in despair',
    '89. The strength of a family is in its unity, a bond that cannot be broken',
    '90. The light of the morning sun brings hope and renewal, a fresh start to each day',
    '91. The whispers of the heart are the truest guide we have on our journey through life',
    '92. The beauty of the world is in its diversity, a tapestry of cultures, colors, and traditions',
    '93. The power of dreams is in their ability to inspire us to reach for the stars',
    '94. The strength of love is in its ability to heal, nurture, and bring us together',
    '95. The warmth of a touch can convey more than words ever could, a language all its own',
    '96. The beauty of the night sky is a reminder of the vastness of the universe and beyond',
    '97. The power of forgiveness is in its ability to free us from the chains of the past',
    '98. The strength of a community is in its unity, a bond that supports and uplifts each member',
    '99. The light of the stars guides us through the darkness, a beacon of hope and possibility'
]


def start_timer():
  return time.time()


def stop_timer(start_time):
  end_time = time.time()
  elapsed_time = end_time - start_time
  return elapsed_time


def compare_phrases(phrase, usr_input):
  correct_count = 0
  incorrect_count = 0

  for i in range(len(usr_input)):
    if i < len(phrase):
      if usr_input[i] == phrase[i]:
        correct_count += 1
      else:
        incorrect_count += 1
    else:
      incorrect_count += 1

  incorrect_count += len(phrase) - len(usr_input)

  return correct_count, incorrect_count


def whrite(phrase):
  start_time = start_timer()
  usr_input = input('-')
  elapsed_time = stop_timer(start_time)

  incorrect_count, correct_count = compare_phrases(phrase, usr_input)

  print('--Results--')
  print('Speed: ', int(elapsed_time), 'segundos')
  print(correct_count, 'Correct written words and',
        int(incorrect_count) - 3, 'incorrect')


def MAIN():
  x = input('Do you want to select a phrase or you will go random? (s/r): ')
  print('----')
  if x == 's':
    phrase = phrases[int(input('Enter a phrase: ')) - 1]
  elif x == 'r':
    phrase = phrases[random.randint(0, 99)]
  else:
    phrase = MAIN()
  return phrase


print(
    '         ,_  o_|_ o        _,      ,       _  _  _|      _|_  _  , _|_ \n|  |  |_/  | | |  | /|/|  / |     / \_|/\_|/ |/ / |       |  |/ / \_|  \n \/ \/     |/|/|_/|/ | |_/\/|/     \/ |_/ |_/|_/\/|_/     |_/|_/ \/ |_/\n                           (|        (|                               '
)
print('Welcome!')
phrase = MAIN()
print(phrase)
print('----')
print('Whrite it as fast as you can! The challenge starts in...')
print('3!')
time.sleep(1)
print('2!')
time.sleep(1)
print('1!')
time.sleep(1)
print('GO!')
whrite(phrase)
