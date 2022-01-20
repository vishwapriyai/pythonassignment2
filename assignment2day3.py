{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "34101ddc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "length of the list:1\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"length of the list:\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e76c42a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "list=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2ae7f580",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your name:vishwa priya.I\n",
      "details: ['vishwa priya.I']\n"
     ]
    }
   ],
   "source": [
    "for i in range(n):\n",
    "    element=input(\"enter your name:\")\n",
    "    list.append(element)\n",
    "print(\"details:\",list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f5a5f07c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your age:18\n",
      "details: ['vishwa priya.I', 18]\n"
     ]
    }
   ],
   "source": [
    "for i in range(n):\n",
    "    element=int(input(\"enter your age:\"))\n",
    "    list.append(element)\n",
    "print(\"details:\",list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "273c4fe2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your destigination:Tamilnadu\n",
      "details: ['vishwa priya.I', 18, 'Tamilnadu']\n"
     ]
    }
   ],
   "source": [
    "for i in range(n):\n",
    "    element=input(\"enter your destigination:\")\n",
    "    list.append(element)\n",
    "print(\"details:\",list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7b83e8f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your qualification:under graduate\n",
      "details: ['vishwa priya.I', 18, 'Tamilnadu', 'under graduate']\n"
     ]
    }
   ],
   "source": [
    "for i in range(n):\n",
    "    element=input(\"enter your qualification:\")\n",
    "    list.append(element)\n",
    "print(\"details:\",list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bc485480",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your college that you are studing:karpaga vinayaga college of engineering and technology\n",
      "details: ['vishwa priya.I', 18, 'Tamilnadu', 'under graduate', 'karpaga vinayaga college of engineering and technology']\n"
     ]
    }
   ],
   "source": [
    "for i in range(n):\n",
    "    element=input(\"enter your college that you are studing:\")\n",
    "    list.append(element)\n",
    "print(\"details:\",list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "27a08e30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the course that you are studind:Btech in artificial intelligence and data science\n",
      "details: ['vishwa priya.I', 18, 'Tamilnadu', 'under graduate', 'karpaga vinayaga college of engineering and technology', 'Btech in artificial intelligence and data science']\n"
     ]
    }
   ],
   "source": [
    "for i in range(n):\n",
    "    element=input(\"enter the course that you are studind:\")\n",
    "    list.append(element)\n",
    "print(\"details:\",list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2129693e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the job you are interested in:data scientist\n",
      "details: ['vishwa priya.I', 18, 'Tamilnadu', 'under graduate', 'karpaga vinayaga college of engineering and technology', 'Btech in artificial intelligence and data science', 'data scientist']\n"
     ]
    }
   ],
   "source": [
    "for i in range(n):\n",
    "    element=input(\"enter the job you are interested in:\")\n",
    "    list.append(element)\n",
    "print(\"details:\",list)"
   ]
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
