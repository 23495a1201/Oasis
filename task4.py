{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c1033d83-08d0-40b3-b8ee-e56550c81591",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dc773ae1-065c-40cf-93b3-9316adbcabea",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"C:/Users/rlsam/Desktop/Oasis/spam.csv\",encoding='latin-1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4cf25d56-eb47-46df-a623-f34cd5770972",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "      <th>Unnamed: 2</th>\n",
       "      <th>Unnamed: 3</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>spam</td>\n",
       "      <td>FreeMsg Hey there darling it's been 3 week's n...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>ham</td>\n",
       "      <td>Even my brother is not like to speak with me. ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>ham</td>\n",
       "      <td>As per your request 'Melle Melle (Oru Minnamin...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>spam</td>\n",
       "      <td>WINNER!! As a valued network customer you have...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>spam</td>\n",
       "      <td>Had your mobile 11 months or more? U R entitle...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     v1                                                 v2 Unnamed: 2  \\\n",
       "0   ham  Go until jurong point, crazy.. Available only ...        NaN   \n",
       "1   ham                      Ok lar... Joking wif u oni...        NaN   \n",
       "2  spam  Free entry in 2 a wkly comp to win FA Cup fina...        NaN   \n",
       "3   ham  U dun say so early hor... U c already then say...        NaN   \n",
       "4   ham  Nah I don't think he goes to usf, he lives aro...        NaN   \n",
       "5  spam  FreeMsg Hey there darling it's been 3 week's n...        NaN   \n",
       "6   ham  Even my brother is not like to speak with me. ...        NaN   \n",
       "7   ham  As per your request 'Melle Melle (Oru Minnamin...        NaN   \n",
       "8  spam  WINNER!! As a valued network customer you have...        NaN   \n",
       "9  spam  Had your mobile 11 months or more? U R entitle...        NaN   \n",
       "\n",
       "  Unnamed: 3 Unnamed: 4  \n",
       "0        NaN        NaN  \n",
       "1        NaN        NaN  \n",
       "2        NaN        NaN  \n",
       "3        NaN        NaN  \n",
       "4        NaN        NaN  \n",
       "5        NaN        NaN  \n",
       "6        NaN        NaN  \n",
       "7        NaN        NaN  \n",
       "8        NaN        NaN  \n",
       "9        NaN        NaN  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "03c69c98-191c-4629-8976-19ed897ff961",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5572, 5)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d54178ba-27d4-4d53-9762-df1bdc926f58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27860"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a0e386c2-f641-4b79-bd04-43163d3c0fba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 5572 entries, 0 to 5571\n",
      "Data columns (total 5 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   v1          5572 non-null   object\n",
      " 1   v2          5572 non-null   object\n",
      " 2   Unnamed: 2  50 non-null     object\n",
      " 3   Unnamed: 3  12 non-null     object\n",
      " 4   Unnamed: 4  6 non-null      object\n",
      "dtypes: object(5)\n",
      "memory usage: 217.8+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b80057e9-a4ba-4d44-9990-8b99e4a9fb61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "      <th>Unnamed: 2</th>\n",
       "      <th>Unnamed: 3</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>5572</td>\n",
       "      <td>5572</td>\n",
       "      <td>50</td>\n",
       "      <td>12</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>2</td>\n",
       "      <td>5169</td>\n",
       "      <td>43</td>\n",
       "      <td>10</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>ham</td>\n",
       "      <td>Sorry, I'll call later</td>\n",
       "      <td>bt not his girlfrnd... G o o d n i g h t . . .@\"</td>\n",
       "      <td>MK17 92H. 450Ppw 16\"</td>\n",
       "      <td>GNT:-)\"</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>4825</td>\n",
       "      <td>30</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          v1                      v2  \\\n",
       "count   5572                    5572   \n",
       "unique     2                    5169   \n",
       "top      ham  Sorry, I'll call later   \n",
       "freq    4825                      30   \n",
       "\n",
       "                                               Unnamed: 2  \\\n",
       "count                                                  50   \n",
       "unique                                                 43   \n",
       "top      bt not his girlfrnd... G o o d n i g h t . . .@\"   \n",
       "freq                                                    3   \n",
       "\n",
       "                   Unnamed: 3 Unnamed: 4  \n",
       "count                      12          6  \n",
       "unique                     10          5  \n",
       "top      MK17 92H. 450Ppw 16\"    GNT:-)\"  \n",
       "freq                        2          2  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9f9cd537-535c-4f96-936a-17110d2fb0b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#drop Last three column(Unnamed:2,Unnamed:3,Unnamed:4) because these columns contain 50,12,6 non-null value out of 5572\n",
    "df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ee871de7-1b66-4e17-956f-ede41939d479",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2461</th>\n",
       "      <td>ham</td>\n",
       "      <td>Anything lar...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1424</th>\n",
       "      <td>ham</td>\n",
       "      <td>Yes.. now only saw your message..</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1837</th>\n",
       "      <td>ham</td>\n",
       "      <td>And how's your husband.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2125</th>\n",
       "      <td>ham</td>\n",
       "      <td>Sorry im getting up now, feel really bad- tota...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       v1                                                 v2\n",
       "2461  ham                                    Anything lar...\n",
       "1424  ham                  Yes.. now only saw your message..\n",
       "1837  ham                            And how's your husband.\n",
       "2125  ham  Sorry im getting up now, feel really bad- tota..."
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sample(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "08778da9-2431-4f91-82a2-776481f4ca23",
   "metadata": {},
   "outputs": [],
   "source": [
    "#renaming the cols\n",
    "df.rename(columns={'v1':'Target','v2':'Text'},inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2ff53559-6e78-4b77-927b-42176bedc924",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2132</th>\n",
       "      <td>spam</td>\n",
       "      <td>Your B4U voucher w/c 27/03 is MARSMS. Log onto...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3406</th>\n",
       "      <td>ham</td>\n",
       "      <td>Beautiful Truth against Gravity.. Read careful...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1990</th>\n",
       "      <td>ham</td>\n",
       "      <td>HI DARLIN IVE JUST GOT BACK AND I HAD A REALLY...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2082</th>\n",
       "      <td>ham</td>\n",
       "      <td>I'm done oredi...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Target                                               Text\n",
       "2132   spam  Your B4U voucher w/c 27/03 is MARSMS. Log onto...\n",
       "3406    ham  Beautiful Truth against Gravity.. Read careful...\n",
       "1990    ham  HI DARLIN IVE JUST GOT BACK AND I HAD A REALLY...\n",
       "2082    ham                                  I'm done oredi..."
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sample(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "33160e90-253e-4343-99fe-fbb185f04def",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "encoder=LabelEncoder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ffbf2594-3392-41f0-b4ac-5ec06f1452db",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Target']=encoder.fit_transform(df['Target'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "09917ad3-7a1b-428a-975e-dd5220f7ef8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>FreeMsg Hey there darling it's been 3 week's n...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0</td>\n",
       "      <td>Even my brother is not like to speak with me. ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>0</td>\n",
       "      <td>As per your request 'Melle Melle (Oru Minnamin...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1</td>\n",
       "      <td>WINNER!! As a valued network customer you have...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1</td>\n",
       "      <td>Had your mobile 11 months or more? U R entitle...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Target                                               Text\n",
       "0       0  Go until jurong point, crazy.. Available only ...\n",
       "1       0                      Ok lar... Joking wif u oni...\n",
       "2       1  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3       0  U dun say so early hor... U c already then say...\n",
       "4       0  Nah I don't think he goes to usf, he lives aro...\n",
       "5       1  FreeMsg Hey there darling it's been 3 week's n...\n",
       "6       0  Even my brother is not like to speak with me. ...\n",
       "7       0  As per your request 'Melle Melle (Oru Minnamin...\n",
       "8       1  WINNER!! As a valued network customer you have...\n",
       "9       1  Had your mobile 11 months or more? U R entitle..."
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c7362cc0-ab2d-4bee-a3f0-1551d67f964f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "403"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking the missing values\n",
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c3ca5f93-5b27-4abf-b8fc-8b4697ac9fed",
   "metadata": {},
   "outputs": [],
   "source": [
    "#remove the duplicates\n",
    "df=df.drop_duplicates(keep='first')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "78cba6e1-a8bc-4904-9454-463f3fdd5719",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d2f27ffa-3b9a-4304-8c99-41bddbd0d185",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5169, 2)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f067ad63-fc19-4abf-95e9-787d7b606b03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>FreeMsg Hey there darling it's been 3 week's n...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0</td>\n",
       "      <td>Even my brother is not like to speak with me. ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>0</td>\n",
       "      <td>As per your request 'Melle Melle (Oru Minnamin...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1</td>\n",
       "      <td>WINNER!! As a valued network customer you have...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1</td>\n",
       "      <td>Had your mobile 11 months or more? U R entitle...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Target                                               Text\n",
       "0       0  Go until jurong point, crazy.. Available only ...\n",
       "1       0                      Ok lar... Joking wif u oni...\n",
       "2       1  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3       0  U dun say so early hor... U c already then say...\n",
       "4       0  Nah I don't think he goes to usf, he lives aro...\n",
       "5       1  FreeMsg Hey there darling it's been 3 week's n...\n",
       "6       0  Even my brother is not like to speak with me. ...\n",
       "7       0  As per your request 'Melle Melle (Oru Minnamin...\n",
       "8       1  WINNER!! As a valued network customer you have...\n",
       "9       1  Had your mobile 11 months or more? U R entitle..."
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e46ff2f8-b5d4-4544-9dab-9db99bb5f901",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5562</th>\n",
       "      <td>0</td>\n",
       "      <td>Ok lor... Sony ericsson salesman... I ask shuh...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5563</th>\n",
       "      <td>0</td>\n",
       "      <td>Ard 6 like dat lor.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5564</th>\n",
       "      <td>0</td>\n",
       "      <td>Why don't you wait 'til at least wednesday to ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5565</th>\n",
       "      <td>0</td>\n",
       "      <td>Huh y lei...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5566</th>\n",
       "      <td>1</td>\n",
       "      <td>REMINDER FROM O2: To get 2.50 pounds free call...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>1</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>0</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>0</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>0</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>0</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Target                                               Text\n",
       "5562       0  Ok lor... Sony ericsson salesman... I ask shuh...\n",
       "5563       0                                Ard 6 like dat lor.\n",
       "5564       0  Why don't you wait 'til at least wednesday to ...\n",
       "5565       0                                       Huh y lei...\n",
       "5566       1  REMINDER FROM O2: To get 2.50 pounds free call...\n",
       "5567       1  This is the 2nd time we have tried 2 contact u...\n",
       "5568       0              Will Ì_ b going to esplanade fr home?\n",
       "5569       0  Pity, * was in mood for that. So...any other s...\n",
       "5570       0  The guy did some bitching but I acted like i'd...\n",
       "5571       0                         Rofl. Its true to its name"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d8efc3ad-1af2-466b-83ea-106c7456958d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Target\n",
       "0    4516\n",
       "1     653\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Target'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "05b80c76-a46e-48f4-92c4-481cb635ebc7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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LKjBF3uPY8PhCpyo42qy7hLkZ8DQzlEY2S0GY3vGoWssL2gjz2FBkMflVDRic3YlNmdXYVuemavKXgC9DsjsFI4R3WIwIj0Wgy6JhL9RLzoW+QgWBHmVzeFCVmENtuaZsSPfjJ+KatHicImOpSipUcEY0S0GI9NjcHnXGIQHc6E8EoMFQULZHC7sLanFjvxqbM+vxr6SWtQ22UXH8poAox7d4k3oER+GgZdEYGR6LDfiIcVgQZDiVDRYkV3eiGPlDThW3ojs8gYcK29Avcqv6E6ODELPhFD0TAhDz8RQ9EwIRecYEwy8aI0UigVBqlFebz2jNHIqGhVVHP5GPeLDApAYHoTu8abWMkgIRY+EUO6pQKrDgiDVs9qdqGmywdxoQ02TDdWW1j9XW2wwW2yosZz8cwuqLTZYWpyADtAB0OkAvU7385910J36dx30up//DUBIgBGRwX6IDPFHVLA/IoL9ERXih2hTABLCAhEfFoiE8EBEhfiL/Y9B5EYsCCIiksX5ckREJIsFQUREslgQREQkiwVBRESyWBBERCSLBUFERLJYEEREJIsFQUREslgQREQkiwVBRESyWBBERCSLBUFERLJYEEREJIsFQUREslgQREQkiwVBRESyWBBERCSLBUFERLJYEEREJIsFQUREslgQREQkiwVBRESyWBBERCSLBUFERLJYEEREJIsFQUREslgQREQkiwVBRESyWBBERCSLBUFERLJYEEREJIsFQUREslgQREQkiwVBRESyWBBERCSLBUFERLJYEEREJIsFQUREslgQREQkiwVBRESyWBBERCSLBUFERLJYEEREJIsFQUREslgQREQkiwVBRESy/h8okYyvK12WFwAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.pie(df['Target'].value_counts(),labels=['ham','spam'],autopct='%0.2f')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "d8a11eb9-3fcc-4073-a306-eb3776577c46",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nltk in c:\\users\\rlsam\\anaconda3\\lib\\site-packages (3.8.1)\n",
      "Requirement already satisfied: click in c:\\users\\rlsam\\anaconda3\\lib\\site-packages (from nltk) (8.1.7)\n",
      "Requirement already satisfied: joblib in c:\\users\\rlsam\\anaconda3\\lib\\site-packages (from nltk) (1.2.0)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\rlsam\\anaconda3\\lib\\site-packages (from nltk) (2023.10.3)\n",
      "Requirement already satisfied: tqdm in c:\\users\\rlsam\\anaconda3\\lib\\site-packages (from nltk) (4.65.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\rlsam\\anaconda3\\lib\\site-packages (from click->nltk) (0.4.6)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\anaconda_navigator-2.5.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\archspec-0.2.1.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\conda-24.1.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\anaconda_navigator-2.5.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\archspec-0.2.1.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\conda-24.1.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\anaconda_navigator-2.5.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\archspec-0.2.1.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\conda-24.1.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\anaconda_navigator-2.5.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\archspec-0.2.1.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\conda-24.1.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\anaconda_navigator-2.5.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\archspec-0.2.1.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\conda-24.1.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\anaconda_navigator-2.5.2.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\archspec-0.2.1.dist-info due to invalid metadata entry 'name'\n",
      "WARNING: Skipping C:\\Users\\rlsam\\anaconda3\\Lib\\site-packages\\conda-24.1.2.dist-info due to invalid metadata entry 'name'\n"
     ]
    }
   ],
   "source": [
    "!pip install nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "04d7d215-c80a-4a72-9e0d-aea01c9f44cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d0ab48cc-b7ed-4b91-9a6e-b028dbf1daa7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\rlsam\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download('punkt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3eec2465-9149-48c8-85da-e7b444b0578e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       111\n",
       "1        29\n",
       "2       155\n",
       "3        49\n",
       "4        61\n",
       "       ... \n",
       "5567    161\n",
       "5568     37\n",
       "5569     57\n",
       "5570    125\n",
       "5571     26\n",
       "Name: Text, Length: 5169, dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#see how to calculate no.of characters in sms/email\n",
    "df['Text'].apply(len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9d99ada4-eaef-4927-8177-c8491e6fc982",
   "metadata": {},
   "outputs": [],
   "source": [
    "#then I store the no.of characters in new variable/col..\n",
    "df['num_characters']=df['Text'].apply(len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "1db18c17-c26d-443c-83d8-d932ea0f5c17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "      <th>num_characters</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>FreeMsg Hey there darling it's been 3 week's n...</td>\n",
       "      <td>148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0</td>\n",
       "      <td>Even my brother is not like to speak with me. ...</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>0</td>\n",
       "      <td>As per your request 'Melle Melle (Oru Minnamin...</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1</td>\n",
       "      <td>WINNER!! As a valued network customer you have...</td>\n",
       "      <td>158</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1</td>\n",
       "      <td>Had your mobile 11 months or more? U R entitle...</td>\n",
       "      <td>154</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Target                                               Text  num_characters\n",
       "0       0  Go until jurong point, crazy.. Available only ...             111\n",
       "1       0                      Ok lar... Joking wif u oni...              29\n",
       "2       1  Free entry in 2 a wkly comp to win FA Cup fina...             155\n",
       "3       0  U dun say so early hor... U c already then say...              49\n",
       "4       0  Nah I don't think he goes to usf, he lives aro...              61\n",
       "5       1  FreeMsg Hey there darling it's been 3 week's n...             148\n",
       "6       0  Even my brother is not like to speak with me. ...              77\n",
       "7       0  As per your request 'Melle Melle (Oru Minnamin...             160\n",
       "8       1  WINNER!! As a valued network customer you have...             158\n",
       "9       1  Had your mobile 11 months or more? U R entitle...             154"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "da2adecb-6efe-4e9b-a12c-8b29840cec7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       [Go, until, jurong, point, ,, crazy, .., Avail...\n",
       "1                [Ok, lar, ..., Joking, wif, u, oni, ...]\n",
       "2       [Free, entry, in, 2, a, wkly, comp, to, win, F...\n",
       "3       [U, dun, say, so, early, hor, ..., U, c, alrea...\n",
       "4       [Nah, I, do, n't, think, he, goes, to, usf, ,,...\n",
       "                              ...                        \n",
       "5567    [This, is, the, 2nd, time, we, have, tried, 2,...\n",
       "5568     [Will, Ì_, b, going, to, esplanade, fr, home, ?]\n",
       "5569    [Pity, ,, *, was, in, mood, for, that, ., So, ...\n",
       "5570    [The, guy, did, some, bitching, but, I, acted,...\n",
       "5571                  [Rofl, ., Its, true, to, its, name]\n",
       "Name: Text, Length: 5169, dtype: object"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#now fetch no.of words\n",
    "df['Text'].apply(lambda x:nltk.word_tokenize(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "adfa7b2e-dc85-4c66-b56b-cbda1c32e59e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       24\n",
       "1        8\n",
       "2       37\n",
       "3       13\n",
       "4       15\n",
       "        ..\n",
       "5567    35\n",
       "5568     9\n",
       "5569    15\n",
       "5570    27\n",
       "5571     7\n",
       "Name: Text, Length: 5169, dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#now I will cal. length of each list\n",
    "df['Text'].apply(lambda x:len(nltk.word_tokenize(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "25c76cf2-6a0e-464e-a282-b665f9fbf8af",
   "metadata": {},
   "outputs": [],
   "source": [
    "#store no. of words in new variable/col. num_words\n",
    "df['num_words']=df['Text'].apply(lambda x:len(nltk.word_tokenize(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e1eca858-5c06-4f79-a2c1-2b65ff02d136",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "      <th>num_characters</th>\n",
       "      <th>num_words</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>111</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>29</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>155</td>\n",
       "      <td>37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>49</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>61</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>FreeMsg Hey there darling it's been 3 week's n...</td>\n",
       "      <td>148</td>\n",
       "      <td>39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0</td>\n",
       "      <td>Even my brother is not like to speak with me. ...</td>\n",
       "      <td>77</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>0</td>\n",
       "      <td>As per your request 'Melle Melle (Oru Minnamin...</td>\n",
       "      <td>160</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1</td>\n",
       "      <td>WINNER!! As a valued network customer you have...</td>\n",
       "      <td>158</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1</td>\n",
       "      <td>Had your mobile 11 months or more? U R entitle...</td>\n",
       "      <td>154</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Target                                               Text  num_characters  \\\n",
       "0       0  Go until jurong point, crazy.. Available only ...             111   \n",
       "1       0                      Ok lar... Joking wif u oni...              29   \n",
       "2       1  Free entry in 2 a wkly comp to win FA Cup fina...             155   \n",
       "3       0  U dun say so early hor... U c already then say...              49   \n",
       "4       0  Nah I don't think he goes to usf, he lives aro...              61   \n",
       "5       1  FreeMsg Hey there darling it's been 3 week's n...             148   \n",
       "6       0  Even my brother is not like to speak with me. ...              77   \n",
       "7       0  As per your request 'Melle Melle (Oru Minnamin...             160   \n",
       "8       1  WINNER!! As a valued network customer you have...             158   \n",
       "9       1  Had your mobile 11 months or more? U R entitle...             154   \n",
       "\n",
       "   num_words  \n",
       "0         24  \n",
       "1          8  \n",
       "2         37  \n",
       "3         13  \n",
       "4         15  \n",
       "5         39  \n",
       "6         18  \n",
       "7         31  \n",
       "8         32  \n",
       "9         31  "
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "9b00394f-eaef-46f6-bbee-2b932768d3cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "      <th>num_characters</th>\n",
       "      <th>num_words</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>1</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "      <td>161</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>0</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "      <td>37</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>0</td>\n",
