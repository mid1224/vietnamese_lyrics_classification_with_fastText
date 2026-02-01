import re

input_file = "final_dataset_test_translated.txt" 
output_file = "final_dataset_test_finished.txt"

need_to_remove = "aaaaaa, tara, artista, ave, bae, baegman, bailar, rolex, belle, de, duh, est, et, gene, laying, tino, eric, erik, mario, mic, pizza, rambo, randy, romeo, ronaldo, tango, tarzan, taxi, tommy, tottenham, wayne, cuo, chuye, zalo, phiu, aaaaaaa,pak, para, phi, pho, phu, qu, rhyder, rhymastic, rong, ru, sa, sam, san, aao, acy, adin, aie, ak, akay, akayz, aku, aldeon, amee, andiez, andree, anhallae, antifan, ap, au, ava, axn, ay, bb, beem, bigboi, bigdaddy, bih, bingboong, bitchen, bla, blacka, blackbi, bmf, bnj, bodan, boodely, bomya, buffely, bulkke, bun, buna, bomyah, woah, woo, yeee, yejeone, ymark, zonnie, zpoet, bung, buoong, cadie, caster, cench, ch, chatjima, cheogirado, chibi, chirstmas, chistmas, choppa, clb, clef, clow, com, comford, comin, conan, culi, cus, daband, dalena, dasi, dc, deodo, deoldo, dg, dicky, didn, dimba, dingdong, dizz, dk, dolil, dou, dsmall, dun, ehhh, ei, eiii, ell, encor, eq, everet, ew, eyy, fallingg, fc, fck, fckin, fen, fm, freakin, gabana, gank, gd, gen, gettin, ghanh, goll, grap, groovin, grrt, guuu, hakoota, haiss, hah, hahahahaha, hallae, haneun, hari, heh, heily, hem, hennest, hia, hihi, hii, hirn, hkt, hmmm, hnay, hooh, hoppin, hrih, hsinh, huh, hustlang, huyr, hwa, hy, icm, ig, ih, ije, il, imma, insaneun, isn, issa, iya, jallan, jallaseo, jang, jc, jenoo, jeoldae, jete, jian, jie, jinx, jiruhae, jiruhal, jiu, jombie, juki, juky, junfuni, juun, juyy, kayc, kdv, keepin, kenbi, keng, kewtie, khovs, kiki, killin, kiu, kn, kuan, kull, kungjuni, ky, lalalala, lalalalala, lbh, ld, lem, leng, lia, lian, lio, liya, lk, lkq, ll, lm, lor, lt, ltb, lum, lun, luu, lvk, ly, lyly, lynk, maesungan, mah, maib, majuchimyeon, malgo, malhalge, mamdaero, mani, marly, mashup, mc, mck, meotdaero, micky, mlee, mlem, mma, momy, movin, movier, mpv, nae, naega, nah, nareul, naro, navidad, necessita, neva, nevana, newfeed, newmusic, northside, nukan, ny, ohhh, ohhhh, okeii, okela, okie, onlyc, oohhh, opps, otd, otit, ouh, overdosee, packka, pangpang, papamama, paparazi, peper, pharreal, pin, pinkky, poca, polyme, pout, powerk, ppeonhan, puku, quihotel, rapital, rastz, rhy, rtee, saero, saeroun, saka, sapa, seachains, sera, serai, shang, sharanghea, sigan, simjange, siro, skiddly, skrt, spaceboiz, taeeonal, taeeonaneun, taeeonaseo, tavak, teum, tivi, tok, tobby, uoh, uohuoh, uuh, vali, vbk, viggas, vinz, vnsound, voient, voudras, vrt, vvs, winx, woh, wonhae, wonhaneun, woring, wowwo, wowy, wssup, yamix, yanbi, yay, yeahh, yeh, yooo, yuh, a, ailes, akira, amour, ano, appelle, autrefois, avec, aww, babushka, bada, baga, bak, bamba, baneunghae, baybe, bayby, bei, biang, bida, blancs, bya, certains, chambre, champage, chardannay, co, comme, comprendras, continuer, coold, cora, cornetto, croire, dangyeonhae, dans, dao, dats, depuis, des, deus, dieu, dudududu, duongk, eh, elle, elles, en, encore, enfin, entre, eodiya, eopseul, eopseulgeoya, eopseunikka, eottae, eotteokae, ey, fait, faut, felicidad, feng, festive, flepy, fondent, gamtanhae, geol, geoya, geum, geureom, gibuniya, giesu, gimbap, gonzo, gracia, grands, ciel, cinta, guhaejwo, guo, hae, hagi, hago, haiz, hana, haru, hee, helia, henny, heundeureojwo, heure, histoire, hoh, hoo, hoonca, igijeogirajiman, ihae, iu, jackie, jager, jagermeister, jal, je, ji, jin, jo, jon, jour, jours, ju, justatee, ka, kai, kaity, kaka, kakashi, kamu, kasim, kay, khmer, kun, kygo, ladykillah, lalala, lambada, larmes, laurent, le, lei, les, lina, lonlely, lou, lourd, luo, lv, maeilmaeil, makin, mal, mana, marijane, marlin, mei, mer, mhee, mia, mian, michyeosseo, migos, minionz, minzy, mochi, mofo, moi, mok, momi, mothamyeon, musique, myfriend, nal, nama, nana, napal, naui, nega, neh, nicky, nipe, noo, noong, notre, nous, nqp, ntt, nuages, oceanmob, oie, oke, okey, oneulcheoreom, oneureun, oo, ooh, oops, oplus, opp, oppa, beo, hieuthuhai, hoaprox, huy, huynh, karik, kienphuc, lee, lim, linh, liu, minhon, miu, nhaaa, obito, osad, ou, ouvre, padme, palestin, par, pas, pate, perd, perdu, pes, peto, peur, peut, pharrel, pluie, po, pola, portes, pourquoi, pouvoir, qg, quand, qui, qung, quoanh, raconterai, rhett, ricky, riri, sais, sait, sans, saphir, sara, sarang, saranghae, sari, sativa, sauvignon, secour, secours, ses, seul, seule, shakespare, shen, shi, shinobi, soit, sol, soleil, somali, southside, tada, tak, taynguyensound, temps, tendre, tenikka, teotteuryeo, thichthichthichthich, thoy, thy, tiamo, tiao, tik, tika, tlinh, toujours, tout, tp, tr, travers, trc, triste, tronie, tryin, tryna, ttak, tuo, tuyn, uhmm, umm, una, valse, vayne, vents, ver, vers, versace, vie, vinahouse, vivra, vn, vois, wao, waseonal, wol, wuan, xesi, xiang, xiao, xog, xxxclusive, ya, yah, yahh, yahhh, ye, yea, yeah, yee, yeogi, yeux, yi, yo, yuki, yuno, yup, za, ze, zeeeee, zhui, zina, zuno, suis, ting, viu, yeezy"

def parse_cleanlist(raw_text):
    items = raw_text.split(',')
    
    clean_set = set()
    for item in items:
        clean_set.add(item)
            
    return clean_set

def remove_words():
    blacklist = parse_cleanlist(need_to_remove)

    with open(input_file, 'r', encoding='utf-8') as input, open(output_file, 'w', encoding='utf-8') as output:
        
        for line in input:
            words = re.split(r'(\W+)', line)
            clean_words = []
            
            for word in words:
                if word.lower() in blacklist:
                    clean_words.append(" ") 
                else:
                    clean_words.append(word)
            
            new_line = "".join(clean_words)
            
            output.write(new_line + "\n")
            
    print(f"Completed: {output_file}")

remove_words()