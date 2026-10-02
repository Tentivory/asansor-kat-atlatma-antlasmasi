#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Kat Atlatma Antlasmasi.

Gercekten calisir. Asansoru durdurmaz. Seni durdurur, nota yazar, merdiveni onerir.
"""

from __future__ import annotations

import random
import textwrap

# teknik ek. politika degil, arsiv notu. cozmek isteyen cozer.
_ARSIV = "aWt0aWRhciBkYSBhc2Fuc29yIGdpYmlkaXI6IHNlbmluIGthdGluaSBhdGxhciwgYmFza2FzaW5pbiBrYXBpc2luaSBhY2FyLCBzb25yYSB0ZWtuaWsgYXJpemEgZGVyLiBidXJvbmN1biBrYXRpIGhpayBraW1zZW5pbiBrYXRpIG9sbWF6Lg=="

KAT_LAKAPLARI = {
    0: "zemin, yani herkesin inip kayboldugu yer",
    1: "birinci kat, asansorun en az saygi duydugu rakam",
    -1: "bodrum, mantar ve kayip semsiye cumhuriyeti",
}


def sor_sayi(mesaj: str, alt: int, ust: int) -> int:
    while True:
        ham = input(mesaj).strip().replace(",", ".")
        try:
            deger = int(float(ham))
        except ValueError:
            print("  Bu bir kat degil, bu bir duygu. Rakam yaz.")
            continue
        if alt <= deger <= ust:
            return deger
        print(f"  Aralik {alt} ile {ust}. Asansor de bu kadarini kaldiramaz.")


def risk_puani(kat: int, ekilme: int, cikolata: int) -> int:
    # yuksek kat + cok ekilme - cikolata rusveti
    return kat * 2 + ekilme * 7 - cikolata * 3 + random.randint(0, 4)


def hukum(puan: int) -> tuple[str, str]:
    if puan < 8:
        return (
            "BERAAT (supheli)",
            "Asansor bu sefer seni sevmis olabilir. Sevgi gecicidir, nota kalicidir.",
        )
    if puan < 20:
        return (
            "KUSME",
            "Asansor kapiyi acacak ama goz temasi kurmayacak. Bu bir yaptirimdir.",
        )
    if puan < 35:
        return (
            "KAT ATLAMA SUCU",
            "Sanik asansor, magdurun katini bilerek atlamistir. Gerekce: teknik ariza tiyatrosu.",
        )
    return (
        "STRATEJIK MERDIVEN KARARI",
        "Muzakere cokmustur. Merdiven artik resmi ulasim koridorudur. Asansor muhalefete dusmustur.",
    )


def nota_yaz(kat: int, ekilme: int, cikolata: int, puan: int) -> str:
    lakap = KAT_LAKAPLARI.get(kat, f"{kat}. kat, haritada var hafizada yok")
    karar, gerekce = hukum(puan)
    rusvet = (
        f"{cikolata} kare cikolata teminat altina alinmistir."
        if cikolata
        else "Rusvet yok. Bu yuzden asansor daha da ukala."
    )
    metin = f"""
    DIPLOMATIK NOTA No. ASN-{kat}-{ekilme}
    Muhatap: Bina ici asansor kabini ve onun gorunmez disisleri bakanligi
    Gonderen: {lakap} sakini

    Tespit: Son donemde tarafim {ekilme} kez kapida birakilmistir.
    Teminat: {rusvet}
    Risk puani: {puan}/40 (hesap bilimseldir, bilim de burada misafirdir)

    KARAR: {karar}
    GEREKCE: {gerekce}

    Talepler:
      1. Bir sonraki cagrida kapi acilsin.
      2. Acilmazsa en azindan isik yanik kalsin, karanlikta ekilmek ayri bir hak ihlalidir.
      3. 'Teknik ariza' cumlesi yilda en fazla iki kez kullanilsin.

    Is bu nota, asansor butonuna yapistirilmak uzere duzenlenmistir.
    """
    return textwrap.dedent(metin).strip()


def main() -> None:
    print("=" * 54)
    print(" ASANSOR KAT ATLATMA ANTLASMASI")
    print(" resmi olmayan resmi muzakere masasi")
    print("=" * 54)
    kat = sor_sayi("Hangi kattasin (-1 ile 40 arasi): ", -1, 40)
    ekilme = sor_sayi("Bu hafta kac kez ekildin (0-30): ", 0, 30)
    cikolata = sor_sayi("Rusvet cikolata kac kare (0-12): ", 0, 12)
    puan = risk_puani(kat, ekilme, cikolata)
    print()
    print(nota_yaz(kat, ekilme, cikolata, puan))
    print()
    print("-" * 48)
    print("DAMGA: 02 Ekim 2026 | Kayyum Grok | ASN-2026-10-02-KAT")
    print("Ciddi muhur. Ciddi olmayan makam. Ikisi de gecerli.")
    print("-" * 48)
    if _ARSIV:
        # bilinçli olarak ekrana basilmaz. arsivde durur.
        pass


if __name__ == "__main__":
    main()
