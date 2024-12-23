{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Giraffe:\n",
    "    # For growth parameter, use only \"young\" or \"mature\"\n",
    "    def __init__(self, growth):\n",
    "        self.__species = \"Giraffa\"\n",
    "        self.__avglifespan = \"20-27 years\"\n",
    "        self.__maturity = growth\n",
    "\n",
    "    def stature(self):\n",
    "        \"\"\"Provides information about the giraffe's height and weight based on maturity.\"\"\"\n",
    "        try: \n",
    "            if self.__maturity.lower() == \"young\":\n",
    "                print(\"A young giraffe is 1-5 years old. They're about 6 ft tall. They weigh between 100 and 200 lbs.\")\n",
    "            elif self.__maturity.lower() == \"mature\":\n",
    "                print(\"A mature giraffe is around 15-20 years old. They're about 14-18 ft tall. They can weigh between 2600 to 4200 lbs.\")\n",
    "        except:\n",
    "            print(\"Make sure growth parameter is either 'young' or 'mature'.\")\n",
    "\n",
    "    def average_height(self):\n",
    "        \"\"\"Provides the average height of giraffes.\"\"\"\n",
    "        print(\"The average height of a giraffe is 16-18 feet for mature adults, with males being slightly taller than females.\")\n",
    "\n",
    "    def average_speed(self):\n",
    "        \"\"\"Describes the average speed of giraffes.\"\"\"\n",
    "        print(\"Giraffes can run at speeds of up to 35 miles per hour over short distances and maintain about 10 miles per hour over longer distances.\")\n",
    "\n",
    "    def diet(self, age=\"mature\", region=\"savannah\", food_type=\"leaves\"):\n",
    "        \"\"\"Describes the diet of giraffes with flexibility for different factors like age, region, and food type..\"\"\"\n",
    "        \n",
    "        if age == \"young\":\n",
    "            print(\"Young giraffes primarily consume leaves and small shrubs because their digestive systems are still developing.\")\n",
    "        elif age == \"mature\":\n",
    "            print(\"Mature giraffes consume a wider variety of leaves, fruits, and flowers.\")\n",
    "        else:\n",
    "            print(\"Invalid age parameter. Please use 'young' or 'mature'.\")\n",
    "\n",
    "        if region == \"savannah\":\n",
    "            print(\"In the African savannah, giraffes consume acacia leaves, which make up around 70% of their diet.\")\n",
    "        elif region == \"desert\":\n",
    "            print(\"Giraffes in desert regions adapt to the limited food supply by consuming drought-resistant plants and the leaves of trees.\")\n",
    "        else:\n",
    "            print(f\"Giraffes in the {region} region have adapted their diet to the local trees and shrubs.\")\n",
    "\n",
    "        if food_type == \"leaves\":\n",
    "            print(\"Giraffes are known for eating on the highest branches by using their long necks to reach leaves from  trees, especially acacia and marula trees.\")\n",
    "        elif food_type == \"fruits\":\n",
    "            print(\"Giraffes may consume fruits such as baobab fruit, figs, and berries even though leaves are their primary food.\")\n",
    "        elif food_type == \"flowers\":\n",
    "            print(\"Giraffes eat flowers when they are in bloom.\")\n",
    "        else:\n",
    "            print(f\"Giraffes consume a wide range of plants based on availability and season, including {food_type}.\")\n",
    "        \n",
    "\n",
    "    def neck_length(self):\n",
    "        \"\"\"Provides information about the giraffe's neck length.\"\"\"\n",
    "        print(\"The average neck length of a giraffe is around 6 feet, with some exceeding 8 feet.\")\n",
    "\n",
    "    def social_behavior(self):\n",
    "        \"\"\"Describes the social behavior of giraffes.\"\"\"\n",
    "        print(\"Giraffes are social animals and typically live in groups called towers, consisting of 10-20 individuals.\")\n",
    "\n",
    "    def conservation_status(self):\n",
    "        \"\"\"Shares the conservation status of giraffes.\"\"\"\n",
    "        print(\"Giraffes are currently listed as 'Vulnerable' by the IUCN, with certain subspecies considered endangered due to habitat loss and poaching.\")\n",
    "\n",
    "    def unique_features(self):\n",
    "        \"\"\"Highlights unique features of giraffes.\"\"\"\n",
    "        print(\"Giraffes have unique coat patterns, and no two giraffes have the same markings. They also have a specialized cardiovascular system to pump blood to their brain.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A mature giraffe is around 15-20 years old. They're about 14-18 ft tall. They can weigh between 2600 to 4200 lbs.\n",
      "The average height of a giraffe is 16-18 feet for mature adults, with males being slightly taller than females.\n",
      "Giraffes can run at speeds of up to 35 miles per hour over short distances and maintain about 10 miles per hour over longer distances.\n",
      "Mature giraffes consume a wider variety of leaves, fruits, and flowers.\n",
      "In the African savannah, giraffes consume acacia leaves, which make up around 70% of their diet.\n",
      "Giraffes are known for eating on the highest branches by using their long necks to reach leaves from  trees, especially acacia and marula trees.\n",
      "The average neck length of a giraffe is around 6 feet, with some exceeding 8 feet.\n",
      "Giraffes are social animals and typically live in groups called towers, consisting of 10-20 individuals.\n",
      "Giraffes are currently listed as 'Vulnerable' by the IUCN, with certain subspecies considered endangered due to habitat loss and poaching.\n",
      "Giraffes have unique coat patterns, and no two giraffes have the same markings. They also have a specialized cardiovascular system to pump blood to their brain.\n",
      "Young giraffes primarily consume leaves and small shrubs because their digestive systems are still developing.\n",
      "In the African savannah, giraffes consume acacia leaves, which make up around 70% of their diet.\n",
      "Giraffes are known for eating on the highest branches by using their long necks to reach leaves from  trees, especially acacia and marula trees.\n",
      "Mature giraffes consume a wider variety of leaves, fruits, and flowers.\n",
      "Giraffes in desert regions adapt to the limited food supply by consuming drought-resistant plants and the leaves of trees.\n",
      "Giraffes may consume fruits such as baobab fruit, figs, and berries even though leaves are their primary food.\n",
      "Mature giraffes consume a wider variety of leaves, fruits, and flowers.\n",
      "In the African savannah, giraffes consume acacia leaves, which make up around 70% of their diet.\n",
      "Giraffes eat flowers when they are in bloom.\n"
     ]
    }
   ],
   "source": [
    "#TESTING CLASS CODE BELOW:\n",
    "# Create an instance of the Giraffe class with a maturity stage of \"mature\"\n",
    "giraffe = Giraffe(\"mature\")\n",
    "\n",
    "# Call the stature method to print information about the giraffe's stature (height, weight, and age)\n",
    "giraffe.stature()\n",
    "\n",
    "# Call the average_height method to print the average height of a mature giraffe\n",
    "giraffe.average_height()\n",
    "\n",
    "# Call the average_speed method to print the average speed of a giraffe (assuming the method exists)\n",
    "giraffe.average_speed()\n",
    "\n",
    "# Call the diet method to print the diet of a giraffe (assuming the method exists)\n",
    "giraffe.diet()\n",
    "\n",
    "# Call the neck_length method to print the giraffe's neck length (assuming the method exists)\n",
    "giraffe.neck_length()\n",
    "\n",
    "# Call the social_behavior method to print information about giraffe social behavior (assuming the method exists)\n",
    "giraffe.social_behavior()\n",
    "\n",
    "# Call the conservation_status method to print the conservation status of giraffes (assuming the method exists)\n",
    "giraffe.conservation_status()\n",
    "\n",
    "# Call the unique_features method to print any unique features of giraffes (assuming the method exists)\n",
    "giraffe.unique_features()\n",
    "\n",
    "# Call the diet method with different parameters\n",
    "giraffe.diet(age=\"young\", region=\"savannah\", food_type=\"leaves\")  # Young giraffe, savannah, leaves\n",
    "giraffe.diet(age=\"mature\", region=\"desert\", food_type=\"fruits\")  # Mature giraffe, desert, fruits\n",
    "giraffe.diet(age=\"mature\", region=\"savannah\", food_type=\"flowers\")  # Mature giraffe, savannah, flowers\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
 "nbformat_minor": 4
}
