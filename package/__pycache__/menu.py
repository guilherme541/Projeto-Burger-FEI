a
    ��~b�  �                   @   s$   g d �Z g d�Zg d�Zdd� ZdS ))zX-SaladazX-BurgerzCachorro QuentezMisto QuentezSalada de FrutasZRefrigerantezSuco Natural)�1�2�3�4�5�6�7)�R$10,00r   zR$7,50zR$8,00zR$5,50zR$4,50zR$6,25c              	   C   s�  t d|  ddd����}td� tdtt��D ](}td�t| t| t| �� t�  q,tt	d��}|d	k�rt d|  d
dd���}g }tt	dtd  ��}|�
|� |�
td � |�d�|�� |��  t	d�}|dks�|dkr�t�  nW d   � �q�W d   � n1 �s0    Y  �nn|dk�r�t d|  d
dd���}g }tt	dtd	  ��}|�
|� |�
td	 � |�d�|�� |��  t	d�}|dk�s�|dk�r�t�  nW d   � �q�W d   � n1 �s�0    Y  �n�|dk�r�t d|  d
dd���}g }tt	dtd  ��}|�
|� |�
td � |�d�|�� |��  t	d�}|dk�s\|dk�rdt�  nW d   � �q�W d   � n1 �s�0    Y  �n�|dk�rVt d|  d
dd���}g }tt	dtd  ��}|�
|� |�
td � |�d�|�� |��  t	d�}|dk�s|dk�r"t�  nW d   � �q�W d   � n1 �sH0    Y  �n4|dk�rt d|  d
dd���}g }tt	dtd  ��}|�
|� |�
td � |�d�|�� |��  t	d�}|dk�s�|dk�r�t�  nW d   � �q�W d   � n1 �s0    Y  �nv|dk�r�t d|  d
dd���}g }tt	dtd  ��}|�
|� |�
td � |�d�|�� |��  t	d�}|dk�s�|dk�r�t�  nW d   � �q�W d   � n1 �s�0    Y  n�|dk�r�t d|  d
dd���}g }tt	dtd  ��}|�
|� |�
td � |�d�|�� |��  t	d�}|dk�sR|dk�rZt�  nW d   � �q�W d   � n1 �s�0    Y  |d	krV|dkrV|dkrV|dkrV|dkrV|dkrV|dkrV|dkrVt�  td� qVW d   � n1 �s�0    Y  d S )Nz
./np%s.txt�wzutf-8)�encodingu�   
==============================================
|Código          Produto               Preço |
==============================================
            �    z{0:<15} {1:<20} {2:<15}z9Digite o Codigo do Produto que deseja efetuar o pedido:  �   �az'Digite a Quantidade de %s que deseja:  z{0}
z*Gostaria de adicionar mais produtos? (S/N)�S�s�   �   z
{0}�   �   �   �   �   u/   Não Encontramos esse produto em nosso cardapio)�open�print�range�len�codigo�format�produto�valor�int�input�append�write�close)�c�dados�i�pZnlistaZ
quantidadet   confirmação� r(   �L   c:\Users\guico\OneDrive\Área de Trabalho\Projeto\BurguerFEI\package\menu.py�	novo_menu   s�    

4

4

4

4

4

2

0@r*   N)r   r   r   r*   r(   r(   r(   r)   �<module>   s   