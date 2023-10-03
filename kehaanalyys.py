
import math

mass = float(input("Sisesta kaal: "))
pikkus = float(input("Sisesta pikkus: "))
vanus = float(input("Sisesta vanus:" ))

m_ideaalkaal = (3 * pikkus - 450 + vanus) * 0.25 + 45
n_ideaalkaal = (3 * pikkus - 450 + vanus) * 0.225 + 40.5

m_rasvaprotsent = ((mass - m_ideaalkaal) / mass) * 100 + 15
n_rasvaprotsent = ((mass - n_ideaalkaal) / mass) * 100 + 22

m_tihedus = 8.9 * m_rasvaprotsent + 11 * (100 - m_rasvaprotsent)
n_tihedus = 8.9 * n_rasvaprotsent + 11 * (100 - n_rasvaprotsent)

m_ruumala = mass / m_tihedus
n_ruumala = mass / n_tihedus

pindala = (1000 * mass) ** ((35.75 - math.log10(mass)) / 53.2) * (pikkus ** 0.3 / 3118.2)

print("Mees\n\tideaalkaal: ",round(m_ideaalkaal, 2),"\n\trasvaprotsent: ",round(m_rasvaprotsent, 2),"\n\ttihedus: "
      ,round(m_tihedus, 2),"\n\truumala: ",round(m_ruumala, 3),"\n\tpindala: ",round(pindala, 3))
print("Naine\n\tideaalkaal: ",round(n_ideaalkaal, 2),"\n\trasvaprotsent: ",round(n_rasvaprotsent, 2),"\n\ttihedus: "
      ,round(n_tihedus, 2),"\n\truumala: ",round(n_ruumala, 3),"\n\tpindala: ",round(pindala, 3))