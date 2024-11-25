{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2657bc36-5df0-4be0-9f4c-f6822ff96a10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A baby giraffe is 0-1 years old, nearly 6 feet tall and weighs about 100-150 lbs.\n",
      "A baby giraffe has soft spotted fur and is dependent on its mother for protection and food.\n",
      "The average height of a giraffe is 16-18 feet for mature adults, with males being slightly taller than females.\n",
      "Young giraffes primarily consume leaves and small shrubs because their digestive systems are still developing.\n",
      "In the African savannah, giraffes consume acacia leaves, which make up around 70% of their diet.\n",
      "Giraffes are known for eating on the highest branches by using their long necks to reach leaves from trees, especially acacia and marula trees.\n",
      "Giraffes are social animals and typically live in groups called towers, consisting of 10-20 individuals.\n"
     ]
    }
   ],
   "source": [
    "class BabyGiraffe(Giraffe):\n",
    "    def __init__(self, growth=\"young\"):\n",
    "        super().__init__(growth)\n",
    "\n",
    "    def stature(self):\n",
    "        \"\"\"Override the stature method to provide details for a baby giraffe.\"\"\"\n",
    "        print(\"A baby giraffe is 0-1 years old, nearly 6 feet tall and weighs about 100-150 lbs.\")\n",
    "\n",
    "    def unique_features(self):\n",
    "        \"\"\"Override the unique_features method to give details about a baby giraffe.\"\"\"\n",
    "        print(\"A baby giraffe has soft spotted fur and is dependent on its mother for protection and food.\")\n",
    "        \n",
    "#Example of a BabyGiraffe \n",
    "baby_giraffe = BabyGiraffe()\n",
    "\n",
    "\n",
    "baby_giraffe.stature()  \n",
    "baby_giraffe.unique_features()\n",
    "#below methods from Giraffe class\n",
    "baby_giraffe.average_height()\n",
    "baby_giraffe.diet(age=\"young\")  \n",
    "baby_giraffe.social_behavior()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8eb498e7-04f4-43cd-bf51-07512dca22a1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
