#Import libraries, CSV's and path to the repository directory
import pandas as pd
import numpy as np
import glob

path = 'E:/Documentos/crimen_mex/'

file1 = glob.glob(path + 'IDEFC*.csv')
file2 = glob.glob(path + 'IDVFC*.csv')

#Create DataFrames
df1 = pd.read_csv(file1[0], sep=',', encoding='latin-1')
df2 = pd.read_csv(file2[0], sep=',', encoding='latin-1')

#Discard unused columns
df1.drop(df1[df1['Tipo de delito']=='Extorsión'].index, inplace=True)
df1.drop(df1[df1['Bien jurídico afectado']=='La vida y la Integridad corporal'].index, inplace=True)
df1.drop(df1[df1['Bien jurídico afectado']=='Libertad personal'].index, inplace=True)
df1.drop(df1[df1['Bien jurídico afectado']=='La sociedad'].index, inplace=True)


#Path to the new CSV
path1 = 'E:/Documentos/crimen_mex/crimen_nac.csv'

#Create a new DataFrame with the data from the past 2 DataFrames
df3 = pd.concat([df1,df2], ignore_index=True, sort=False)

#Fill missing information with identifiers
df3['Sexo'] = df3['Sexo'].fillna('Averiguación previa')
df3['Rango de edad'] = df3['Rango de edad'].fillna('No aplica')

#Rename column to add new identifier
df3.rename(columns={'Sexo':'Sexo/Averiguación previa'}, inplace=True)

#Categorize strings in columns to match parameters
df3.loc[df3['Tipo de delito'].str.contains('Feminicidio'), 'Tipo de delito'] = 'Homicidio'
df3.loc[df3['Tipo de delito'].str.contains('Violación'), 'Tipo de delito'] = 'Violación'
df3.loc[df3['Tipo de delito'].str.contains('Hostigamiento sexual'), 'Tipo de delito'] = 'Delito sexual'
df3.loc[df3['Tipo de delito'].str.contains('Acoso sexual'), 'Tipo de delito'] = 'Delito sexual'
df3.loc[df3['Tipo de delito'].str.contains('Abuso sexual'), 'Tipo de delito'] = 'Delito sexual'
df3.loc[df3['Modalidad'].str.contains('Con violencia'), 'Tipo de delito'] = 'Robo con violencia'
df3.loc[df3['Modalidad'].str.contains('Sin violencia'), 'Tipo de delito'] = 'Robo sin violencia'

df3.loc[df3['Modalidad'].str.contains('coche de 4'), 'Subtipo de delito'] = 'Robo de vehículo automotor (4 R)'
df3.loc[df3['Modalidad'].str.contains('motocicleta'), 'Subtipo de delito'] = 'Robo de vehículo automotor (2 R)'
df3.loc[df3['Modalidad'].str.contains('embarcaciones'), 'Subtipo de delito'] = 'Robo de embarcaciones (pequeñas & grandes)'
df3.loc[df3['Modalidad'].str.contains('herramienta industrial'), 'Subtipo de delito'] = 'Robo de maquinaria (herr. indust. o agrícola)'
df3.loc[df3['Modalidad'].str.contains('tractores'), 'Subtipo de delito'] = 'Robo de maquinaria (tractores)'
df3.loc[df3['Modalidad'].str.contains('cables, tubos'), 'Subtipo de delito'] = 'Robo de material destinado a serv. públicos'
df3.loc[df3['Subtipo de delito'].str.contains('transeúnte'), 'Subtipo de delito'] = 'Robo a transeúnte en espacio o vía pública'
df3.loc[df3['Subtipo de delito'].str.contains('transporte público'), 'Subtipo de delito'] = 'Robo en transporte público (indiv. & colect.)'

df3.loc[df3['Modalidad'].str.contains('Secuestro'), 'Subtipo de delito'] = df3['Modalidad']
df3.loc[df3['Modalidad'].str.contains('secuestros'), 'Subtipo de delito'] = df3['Modalidad']

#Discard unused column
df3.drop(columns=['Modalidad'])

#Save new DataFrame in CSV format
df3.to_csv(path1, sep=',', header=True, index=False, encoding='latin-1')


