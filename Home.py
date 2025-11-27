import streamlit as st

st.set_page_config(
    page_title="No Auth API Showcase",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 No Auth API Showcase")

st.markdown("""
### Welcome!
This application showcases **725** public APIs that require no authentication.
Explore them using the sidebar!

### Features
- **No API Keys needed**: Just plug and play.
- **Interactive**: Try out the APIs directly.
- **Massive Collection**: From Animals to Weather, Crypto to Transport.

### API List
""")

with st.expander("View Full List of 725 APIs"):
    st.markdown("""
1. **🐶 Dog Images**
2. **😂 Jokes**
3. **🐱 Cat Facts**
4. **👤 Nationality Predictor**
5. **🏫 University Search**
6. **👶 Age Predictor**
7. **⚧️ Gender Predictor**
8. **🧠 Useless Facts**
9. **💰 Bitcoin Price**
10. **💱 Currency Converter**
11. **📍 IP Info**
12. **🧑 Random User**
13. **💡 Advice Slip**
14. **🧪 Rick and Morty**
15. **🐉 Pokemon Info**
16. **📚 Book Search**
17. **📮 Zip Code Info**
18. **🌤️ Weather**
19. **📖 Dictionary**
20. **🔢 Number Facts**
21. **🍺 Brewery Search**
22. **🦊 Random Fox**
23. **🦆 Random Duck**
24. **💻 Techy Jargon**
25. **👔 Corporate BS**
26. **🤓 Geek Jokes**
27. **🎤 Kanye Quotes**
28. **👺 Anime Quotes**
29. **🍔 Food Images**
30. **☕ Coffee Images**
31. **🐕 Shiba Inu**
32. **👍 Yes No**
33. **🤥 Excuser**
34. **🐱 HTTP Cats**
35. **🤖 RoboHash**
36. **🥱 Bored API**
37. **💬 Quotable**
38. **🌅 Sunrise Sunset**
39. **📺 TV Maze**
40. **🍸 Cocktail DB**
41. **🍲 Meal DB**
42. **💄 Makeup API**
43. **🎨 Art Institute**
44. **🚀 SpaceX**
45. **🐱 PlaceKitten**
46. **📸 Lorem Picsum**
47. **📅 Public Holidays**
48. **👾 Pixel Encounter**
49. **🎲 DiceBear**
50. **🥫 Open Food Facts**
51. **🦎 Axolotl**
52. **🐱 Cataas**
53. **🐶 HTTP Dog**
54. **🦁 Zoo Animals**
55. **🎌 AnimeFacts**
56. **🕵️ Jikan**
57. **🎬 Studio Ghibli**
58. **🖼️ Waifu Pics**
59. **😀 EmojiHub**
60. **🐴 Icon Horse**
61. **📚 Gutendex**
62. **📜 PoetryDB**
63. **📖 Bible API**
64. **💰 CoinCap**
65. **🦎 CoinGecko**
66. **💱 ExchangeRate API**
67. **📊 QuickChart**
68. **🆔 UUID Generator**
69. **🎷 Binary Jazz**
70. **🎵 Lyrics ovh**
71. **🚀 Spaceflight News**
72. **🏛️ Archive org**
73. **🏆 Nobel Prize**
74. **😈 Evil Insult**
75. **🌌 NASA APOD**
76. **🌍 USGS Earthquake**
77. **🚲 CityBikes**
78. **🤥 FakerAPI**
79. **🗣️ LibreTranslate**
80. **🎮 FreeToGame**
81. **🌐 Cat Facts 81**
82. **🌐 Dog Facts**
83. **🌐 Dog Facts 83**
84. **🌐 Dogs**
85. **🌐 FishWatch**
86. **🌐 HTTP Cat**
87. **🌐 HTTP Dog 87**
88. **🌐 MeowFacts**
89. **🌐 Movebank**
90. **🌐 PlaceBear**
91. **🌐 PlaceDog**
92. **🌐 RandomDog**
93. **🌐 RandomDuck**
94. **🌐 RandomFox**
95. **🌐 RescueGroups**
96. **🌐 ShibeOnline**
97. **🌐 xenocanto**
98. **🌐 Zoo Animals 98**
99. **🌐 AnimeChan**
100. **🌐 AnimeNewsNetwork**
101. **🌐 Catboy**
102. **🌐 NekosBest**
103. **🌐 Studio Ghibli 103**
104. **🌐 Trace Moe**
105. **🌐 Waifuim**
106. **🌐 Waifupics**
107. **🌐 URLhaus**
108. **🌐 Art Institute of Chicago**
109. **🌐 Colormind**
110. **🌐 ColourLovers**
111. **🌐 Icon Horse 111**
112. **🌐 Icons8**
113. **🌐 Lordicon**
114. **🌐 Metropolitan Museum of Art**
115. **🌐 PHPNoise**
116. **🌐 Pixel Encounter 116**
117. **🌐 xColors**
118. **🌐 Chainlink**
119. **🌐 Chainpoint**
120. **🌐 Helium**
121. **🌐 Steem**
122. **🌐 Walltime**
123. **🌐 Bhagavad Gita telugu**
124. **🌐 Bibleapi**
125. **🌐 British National Bibliography**
126. **🌐 Crossref Metadata Search**
127. **🌐 GurbaniNow**
128. **🌐 Open Library**
129. **🌐 Penguin Publishing**
130. **🌐 Quran**
131. **🌐 Quran Cloud**
132. **🌐 Quranapi**
133. **🌐 Rig Veda**
134. **🌐 Thirukkural**
135. **🌐 Vedic Society**
136. **🌐 Wizard World**
137. **🌐 Wolne Lektury**
138. **🌐 Tenders in Hungary**
139. **🌐 Tenders in Poland**
140. **🌐 Tenders in Romania**
141. **🌐 Tenders in Spain**
142. **🌐 Tenders in Ukraine**
143. **🌐 Church Calendar**
144. **🌐 Czech Namedays Calendar**
145. **🌐 Hebrew Calendar**
146. **🌐 LectServe**
147. **🌐 NagerDate**
148. **🌐 Namedays Calendar**
149. **🌐 NonWorking Days**
150. **🌐 NonWorking Days 150**
151. **🌐 Russian Calendar**
152. **🌐 UK Bank Holidays**
153. **🌐 AnonFiles**
154. **🌐 BayFiles**
155. **🌐 Fileio**
156. **🌐 Pantry**
157. **🌐 The Null Pointer**
158. **🌐 0x**
159. **🌐 1inch**
160. **🌐 Bitcambio**
161. **🌐 BitcoinCharts**
162. **🌐 CoinDesk**
163. **🌐 Coinlore**
164. **🌐 Coinpaprika**
165. **🌐 CoinStats**
166. **🌐 CryptAPI**
167. **🌐 CryptingUp**
168. **🌐 CryptoCompare**
169. **🌐 Cryptonator**
170. **🌐 Gemini**
171. **🌐 Localbitcoins**
172. **🌐 Mempool**
173. **🌐 MercadoBitcoin**
174. **🌐 Messari**
175. **🌐 Nexchange**
176. **🌐 ZMOK**
177. **🌐 Bank of Russia**
178. **🌐 Currencyapi**
179. **🌐 Czech National Bank**
180. **🌐 EconomiaAwesome**
181. **🌐 Exchangeratehost**
182. **🌐 Frankfurter**
183. **🌐 FreeForexAPI**
184. **🌐 National Bank of Poland**
185. **🌐 VATComplycom**
186. **🌐 Postman Echo**
187. **🌐 PurgoMalum**
188. **🌐 24 Pull Requests**
189. **🌐 Agifyio**
190. **🌐 API Grátis**
191. **🌐 ApicAgent**
192. **🌐 APIsguru**
193. **🌐 Beeceptor**
194. **🌐 Bored**
195. **🌐 CDNJS**
196. **🌐 Changelogsmd**
197. **🌐 Ciprand**
198. **🌐 Cloudflare Trace**
199. **🌐 Codex**
200. **🌐 CORS Proxy**
201. **🌐 CountAPI**
202. **🌐 DigitalOcean Status**
203. **🌐 DomainDb Info**
204. **🌐 ExtendsClass JSON Storage**
205. **🌐 Genderizeio**
206. **🌐 hosttcom**
207. **🌐 HTTP2Pro**
208. **🌐 Httpbin**
209. **🌐 Httpbin Cloudflare**
210. **🌐 Icanhazepoch**
211. **🌐 Icanhazip**
212. **🌐 IFTTT**
213. **🌐 ImageCharts**
214. **🌐 ipfastcom**
215. **🌐 IPify**
216. **🌐 IPinfo**
217. **🌐 jsDelivr**
218. **🌐 JSON 2 JSONP**
219. **🌐 Kroki**
220. **🌐 LicenseAPI**
221. **🌐 Lua Decompiler**
222. **🌐 MicroENV**
223. **🌐 Mocky**
224. **🌐 MY IP**
225. **🌐 Nationalizeio**
226. **🌐 NetworkCalc**
227. **🌐 npm Registry**
228. **🌐 oyyi**
229. **🌐 QR code**
230. **🌐 QR code 230**
231. **🌐 Qrcode Monkey**
232. **🌐 ReqRes**
233. **🌐 RSS feed to JSON**
234. **🌐 Serialif Color**
235. **🌐 SHOUTCLOUD**
236. **🌐 Sonar**
237. **🌐 Statically**
238. **🌐 Wandbox**
239. **🌐 Chinese Character Web**
240. **🌐 Chinese Text Project**
241. **🌐 Free Dictionary**
242. **🌐 Indonesia Dictionary**
243. **🌐 Wiktionary**
244. **🌐 Vector Express v20**
245. **🌐 WakaTime**
246. **🌐 Disify**
247. **🌐 DropMail**
248. **🌐 EVA**
249. **🌐 Guerrilla Mail**
250. **🌐 Kickbox**
251. **🌐 mailgw**
252. **🌐 mailtm**
253. **🌐 MailCheckai**
254. **🌐 chucknorrisio**
255. **🌐 Corporate Buzz Words**
256. **🌐 Fun Fact**
257. **🌐 Imgflip**
258. **🌐 Meme Maker**
259. **🌐 NaMoMemes**
260. **🌐 Random Useless Facts**
261. **🌐 Techy**
262. **🌐 Yo Momma Jokes**
263. **🌐 CO2 Offset**
264. **🌐 Danish data service Energi**
265. **🌐 GrünstromIndex**
266. **🌐 Luchtmeetnet**
267. **🌐 National Grid ESO**
268. **🌐 PM25 Open Data Portal**
269. **🌐 UK Carbon Intensity**
270. **🌐 Website Carbon**
271. **🌐 Binlist**
272. **🌐 Econdb**
273. **🌐 Fed Treasury**
274. **🌐 Portfolio Optimizer**
275. **🌐 Razorpay IFSC**
276. **🌐 SEC EDGAR Data**
277. **🌐 WallstreetBets**
278. **🌐 BaconMockup**
279. **🌐 Coffee**
280. **🌐 Foodish**
281. **🌐 Fruityvice**
282. **🌐 Open Brewery DB**
283. **🌐 Open Food Facts 283**
284. **🌐 PunkAPI**
285. **🌐 Rustybeer**
286. **🌐 TacoFancy**
287. **🌐 The Report of the Week**
288. **🌐 WhiskyHunter**
289. **🌐 Age of Empires II**
290. **🌐 AmiiboAPI**
291. **🌐 Animal Crossing New Horizons**
292. **🌐 Autochess VNG**
293. **🌐 BarterVG**
294. **🌐 Board Game Geek**
295. **🌐 Bugsnax**
296. **🌐 CheapShark**
297. **🌐 Chesscom**
298. **🌐 Chuck Norris Database**
299. **🌐 Comic Vine**
300. **🌐 Crafatar**
301. **🌐 Cross Universe**
302. **🌐 Deck of Cards**
303. **🌐 Digimon Information**
304. **🌐 Digimon TCG**
305. **🌐 Disney**
306. **🌐 Dungeons and Dragons**
307. **🌐 Dungeons and Dragons Alternate**
308. **🌐 FFXIV Collect**
309. **🌐 FIFA Ultimate Team**
310. **🌐 Final Fantasy XIV**
311. **🌐 Forza**
312. **🌐 Fun Facts**
313. **🌐 FunTranslations**
314. **🌐 GamerPower**
315. **🌐 GDBrowser**
316. **🌐 GeekJokes**
317. **🌐 Genshin Impact**
318. **🌐 GraphQL Pokemon**
319. **🌐 GW2Spidy**
320. **🌐 Hyrule Compendium**
321. **🌐 Hytale**
322. **🌐 JokeAPI**
323. **🌐 Jservice**
324. **🌐 Magic The Gathering**
325. **🌐 Minecraft Server Status**
326. **🌐 MMO Games**
327. **🌐 Monster Hunter World**
328. **🌐 Open Trivia**
329. **🌐 PlayerDB**
330. **🌐 Pokéapi**
331. **🌐 PokéAPI GraphQL**
332. **🌐 Pokémon TCG**
333. **🌐 Psychonauts**
334. **🌐 Puyo Nexus**
335. **🌐 Raider**
336. **🌐 Rick and Morty 336**
337. **🌐 RPS 101**
338. **🌐 RuneScape**
339. **🌐 Sakura CardCaptor**
340. **🌐 Scryfall**
341. **🌐 Steam**
342. **🌐 TCGdex**
343. **🌐 TETRIO**
344. **🌐 Tronald Dump**
345. **🌐 Universalis**
346. **🌐 Valorant nonofficial**
347. **🌐 Warface nonofficial**
348. **🌐 When is next MCU film**
349. **🌐 xkcd**
350. **🌐 YuGiOh**
351. **🌐 administrativedivisonsdb**
352. **🌐 adressedatagouvfr**
353. **🌐 Airtel IP**
354. **🌐 Cartesio**
355. **🌐 Cepla**
356. **🌐 CitySDK**
357. **🌐 Country**
358. **🌐 Ducks Unlimited**
359. **🌐 FreeGeoIP**
360. **🌐 GeoApi**
361. **🌐 Geocodexyz**
362. **🌐 Geodatagovgr**
363. **🌐 GeographQL**
364. **🌐 GeoJS**
365. **🌐 Geokeo**
366. **🌐 GeoNames**
367. **🌐 geoPlugin**
368. **🌐 Graph Countries**
369. **🌐 HelloSalut**
370. **🌐 Hong Kong GeoData Store**
371. **🌐 IBGE**
372. **🌐 IP 2 Country**
373. **🌐 IP Address Details**
374. **🌐 IP Vigilante**
375. **🌐 ipapi**
376. **🌐 ipapico**
377. **🌐 IPGEO**
378. **🌐 Mexico**
379. **🌐 Nominatim**
380. **🌐 OnWater**
381. **🌐 Open Topo Data**
382. **🌐 Pinball Map**
383. **🌐 Postali**
384. **🌐 PostcodeDatanl**
385. **🌐 Postcodesio**
386. **🌐 Queimadas INPE**
387. **🌐 REST Countries**
388. **🌐 Rwanda Locations**
389. **🌐 SLF**
390. **🌐 ViaCep**
391. **🌐 Zippopotamus**
392. **🌐 Ziptastic**
393. **🌐 Bank Negara Malaysia Open Data**
394. **🌐 BCLaws**
395. **🌐 Brazil**
396. **🌐 Brazil Central Bank Open Data**
397. **🌐 Brazil Receita WS**
398. **🌐 Brazilian Chamber of Deputies Open Data**
399. **🌐 Censusgov**
400. **🌐 City Berlin**
401. **🌐 City Gdańsk**
402. **🌐 City Gdynia**
403. **🌐 City Helsinki**
404. **🌐 City Lviv**
405. **🌐 City New York Open Data**
406. **🌐 City Prague Open Data**
407. **🌐 City Toronto Open Data**
408. **🌐 Colorado Information Marketplace**
409. **🌐 Data USA**
410. **🌐 Dataparliamentuk**
411. **🌐 District of Columbia Open Data**
412. **🌐 EPA**
413. **🌐 FBI Wanted**
414. **🌐 Federal Register**
415. **🌐 Food Standards Agency**
416. **🌐 INEI**
417. **🌐 Interpol Red Notices**
418. **🌐 Istanbul İBB Open Data**
419. **🌐 Open Government ACT**
420. **🌐 Open Government Argentina**
421. **🌐 Open Government Australia**
422. **🌐 Open Government Austria**
423. **🌐 Open Government Belgium**
424. **🌐 Open Government Canada**
425. **🌐 Open Government Colombia**
426. **🌐 Open Government Cyprus**
427. **🌐 Open Government Czech Republic**
428. **🌐 Open Government Denmark**
429. **🌐 Open Government Finland**
430. **🌐 Open Government Germany**
431. **🌐 Open Government Ireland**
432. **🌐 Open Government Italy**
433. **🌐 Open Government Lithuania**
434. **🌐 Open Government Mexico**
435. **🌐 Open Government Mexico 435**
436. **🌐 Open Government Netherlands**
437. **🌐 Open Government New Zealand**
438. **🌐 Open Government Norway**
439. **🌐 Open Government Peru**
440. **🌐 Open Government Poland**
441. **🌐 Open Government Portugal**
442. **🌐 Open Government Queensland Government**
443. **🌐 Open Government Romania**
444. **🌐 Open Government Saudi Arabia**
445. **🌐 Open Government Singapore**
446. **🌐 Open Government Slovakia**
447. **🌐 Open Government Slovenia**
448. **🌐 Open Government South Australian Government**
449. **🌐 Open Government Spain**
450. **🌐 Open Government Sweden**
451. **🌐 Open Government Switzerland**
452. **🌐 Open Government Taiwan**
453. **🌐 Open Government UK**
454. **🌐 Open Government USA**
455. **🌐 Open Government Victoria State Government**
456. **🌐 Open Government West Australia**
457. **🌐 PRC Exam Schedule**
458. **🌐 Represent by Open North**
459. **🌐 US Presidential Election Data by TogaTech**
460. **🌐 USAspendinggov**
461. **🌐 Coronavirus**
462. **🌐 Coronavirus in the UK**
463. **🌐 Covid Tracking Project**
464. **🌐 Covid19**
465. **🌐 Covid19 465**
466. **🌐 Covid19 Datenhub**
467. **🌐 Covid19 Government Response**
468. **🌐 Covid19 India**
469. **🌐 Covid19 JHU CSSE**
470. **🌐 Covid19 Live Data**
471. **🌐 Covid19 Philippines**
472. **🌐 COVID19 Tracker Canada**
473. **🌐 COVID19 Tracker Sri Lanka**
474. **🌐 COVIDID**
475. **🌐 Dataflow Kit COVID19**
476. **🌐 Healthcaregov**
477. **🌐 Humanitarian Data Exchange**
478. **🌐 LAPIS**
479. **🌐 Makeup**
480. **🌐 MyVaccination**
481. **🌐 NPPES**
482. **🌐 Open Data NHS Scotland**
483. **🌐 Open Disease**
484. **🌐 Quarantine**
485. **🌐 Arbeitnow**
486. **🌐 DevITjobs UK**
487. **🌐 GraphQL Jobs**
488. **🌐 Open Skills**
489. **🌐 Deepcode**
490. **🌐 EXUDEAPI**
491. **🌐 OpenVisionAPI**
492. **🌐 Bandsintown**
493. **🌐 Gaana**
494. **🌐 Genrenator**
495. **🌐 iTunes Search**
496. **🌐 JioSaavn**
497. **🌐 Lyricsovh**
498. **🌐 MusicBrainz**
499. **🌐 Openwhyd**
500. **🌐 Radio Browser**
501. **🌐 Songsterr**
502. **🌐 Chronicling America**
503. **🌐 Graphs for Coronavirus**
504. **🌐 Inshorts News**
505. **🌐 Spaceflight News 505**
506. **🌐 18F**
507. **🌐 API Setu**
508. **🌐 Archiveorg**
509. **🌐 BotsArchive**
510. **🌐 Callookinfo**
511. **🌐 CollegeScoreCardedgov**
512. **🌐 French Address Search**
513. **🌐 Lowy Asia Power Index**
514. **🌐 Microlinkio**
515. **🌐 Nobel Prize 515**
516. **🌐 Open Data Minneapolis**
517. **🌐 openAFRICA**
518. **🌐 OpenSanctions**
519. **🌐 Teleport**
520. **🌐 Umeå Open Data**
521. **🌐 Universities List**
522. **🌐 University of Oslo**
523. **🌐 Urban Observatory**
524. **🌐 Wikipedia**
525. **🌐 Countly**
526. **🌐 Datamuse**
527. **🌐 Drupalorg**
528. **🌐 Evil Insult Generator**
529. **🌐 GitHub Contribution Chart Generator**
530. **🌐 GitHub ReadMe Stats**
531. **🌐 Metabase**
532. **🌐 Shields**
533. **🌐 PatentsView**
534. **🌐 USPTO**
535. **🌐 Advice Slip 535**
536. **🌐 Biriyani As A Service**
537. **🌐 Dictum**
538. **🌐 FOAAS**
539. **🌐 Forismatic**
540. **🌐 icanhazdadjoke**
541. **🌐 Inspiration**
542. **🌐 kanyerest**
543. **🌐 kimiquotes**
544. **🌐 Programming Quotes**
545. **🌐 Quotable Quotes**
546. **🌐 Quote Garden**
547. **🌐 quoteclear**
548. **🌐 Quotes on Design**
549. **🌐 Stoicism Quote**
550. **🌐 They Said So Quotes**
551. **🌐 Traitify**
552. **🌐 Vadivelu HTTP Codes**
553. **🌐 Zen Quotes**
554. **🌐 Phone Specification**
555. **🌐 apilayer screenshotlayer**
556. **🌐 Imsea**
557. **🌐 Lorem Picsum 557**
558. **🌐 PlaceKeanu**
559. **🌐 Readme typing SVG**
560. **🌐 ReSmushit**
561. **🌐 KONTESTS**
562. **🌐 arcsecondio**
563. **🌐 arXiv**
564. **🌐 GBIF**
565. **🌐 iDigBio**
566. **🌐 inspirehepnet**
567. **🌐 isEven humor**
568. **🌐 ISRO**
569. **🌐 ITIS**
570. **🌐 Launch Library 2**
571. **🌐 Minor Planet Center**
572. **🌐 NASA**
573. **🌐 Newton**
574. **🌐 Noctua**
575. **🌐 Numbers**
576. **🌐 Ocean Facts**
577. **🌐 Open Notify**
578. **🌐 Open Science Framework**
579. **🌐 Purple Air**
580. **🌐 Remote Calc**
581. **🌐 SHARE**
582. **🌐 Sunrise and Sunset**
583. **🌐 Times Adder**
584. **🌐 TLE**
585. **🌐 USGS Earthquake Hazards Program**
586. **🌐 USGS Water Services**
587. **🌐 World Bank**
588. **🌐 xMath**
589. **🌐 Classify**
590. **🌐 Dehashlt**
591. **🌐 EmailRep**
592. **🌐 Escape**
593. **🌐 FilterLists**
594. **🌐 Hashable**
595. **🌐 Microsoft Security Response Center MSRC**
596. **🌐 Mozilla http scanner**
597. **🌐 Mozilla tls scanner**
598. **🌐 National Vulnerability Database**
599. **🌐 Passwordinator**
600. **🌐 PhishStats**
601. **🌐 UK Police**
602. **🌐 Virushee**
603. **🌐 4chan**
604. **🌐 aztro**
605. **🌐 DogeMeme**
606. **🌐 Fuck Off as a Service**
607. **🌐 HackerNews**
608. **🌐 Hashnode**
609. **🌐 Lanyard**
610. **🌐 Open Collective**
611. **🌐 balldontlie**
612. **🌐 Ergast F1**
613. **🌐 Football Soccer Videos**
614. **🌐 Football Standings**
615. **🌐 MLB Records and Stats**
616. **🌐 NBA Stats**
617. **🌐 NHL Records and Stats**
618. **🌐 Oddsmagnet**
619. **🌐 OpenLigaDB**
620. **🌐 Sport List  Data**
621. **🌐 Sport Places**
622. **🌐 Squiggle**
623. **🌐 SuredBits**
624. **🌐 Bacon Ipsum**
625. **🌐 Dicebear Avatars**
626. **🌐 English Random Words**
627. **🌐 FakeStoreAPI**
628. **🌐 ItsThisForThat**
629. **🌐 JSONPlaceholder**
630. **🌐 Loripsum**
631. **🌐 Metaphorsum**
632. **🌐 QuickMocker**
633. **🌐 Random Data**
634. **🌐 RandomUser**
635. **🌐 Spanish random names**
636. **🌐 Spanish random words**
637. **🌐 This Person Does not Exist**
638. **🌐 Toolcarton**
639. **🌐 UUID Generator 639**
640. **🌐 What The Commit**
641. **🌐 Yes No 641**
642. **🌐 PostalPinCode**
643. **🌐 Postmon**
644. **🌐 WhatPulse**
645. **🌐 ADSB Exchange**
646. **🌐 airportsapi**
647. **🌐 AviationAPI**
648. **🌐 BC Ferries**
649. **🌐 Community Transit**
650. **🌐 Icelandic APIs**
651. **🌐 Metro Lisboa**
652. **🌐 OpenSky Network**
653. **🌐 REFUGE Restrooms**
654. **🌐 TransitLand**
655. **🌐 Transport for Atlanta US**
656. **🌐 Transport for Auckland New Zealand**
657. **🌐 Transport for Belgium**
658. **🌐 Transport for Berlin Germany**
659. **🌐 Transport for Budapest Hungary**
660. **🌐 Transport for Czech Republic**
661. **🌐 Transport for Denver US**
662. **🌐 Transport for Finland**
663. **🌐 Transport for Grenoble France**
664. **🌐 Transport for Hessen Germany**
665. **🌐 Transport for Los Angeles US**
666. **🌐 Transport for Norway**
667. **🌐 Transport for Paris France**
668. **🌐 Transport for Philadelphia US**
669. **🌐 Transport for Spain**
670. **🌐 Transport for Switzerland**
671. **🌐 Transport for The Netherlands**
672. **🌐 Transport for Toronto Canada**
673. **🌐 Transport for United States**
674. **🌐 transportrest**
675. **🌐 Velib metropolis Paris France**
676. **🌐 1pt**
677. **🌐 CleanURI**
678. **🌐 Drivet URL Shortener**
679. **🌐 Free Url Shortener**
680. **🌐 Gitio**
681. **🌐 GoTiny**
682. **🌐 Mgnetme**
683. **🌐 owo**
684. **🌐 Short Link**
685. **🌐 Shrtcode**
686. **🌐 Brazilian Vehicles and Prices**
687. **🌐 NHTSA**
688. **🌐 An API of Ice And Fire**
689. **🌐 Bobs Burgers**
690. **🌐 Breaking Bad**
691. **🌐 Breaking Bad Quotes**
692. **🌐 Catalogopolis**
693. **🌐 Catch The Show**
694. **🌐 Czech Television**
695. **🌐 Dune**
696. **🌐 Final Space**
697. **🌐 Game of Thrones Quotes**
698. **🌐 Harry Potter Charactes**
699. **🌐 IMDbOT**
700. **🌐 Lucifer Quotes**
701. **🌐 MCU Countdown**
702. **🌐 Motivational Quotes**
703. **🌐 Movie Quote**
704. **🌐 Owen Wilson Wow**
705. **🌐 Ron Swanson Quotes**
706. **🌐 STAPI**
707. **🌐 Stranger Things Quotes**
708. **🌐 Stream**
709. **🌐 Stromberg Quotes**
710. **🌐 SWAPI**
711. **🌐 SWAPI 711**
712. **🌐 SWAPI GraphQL**
713. **🌐 ThronesApi**
714. **🌐 TVMaze**
715. **🌐 Web Series Quotes Generator**
716. **🌐 7Timer**
717. **🌐 AviationWeather**
718. **🌐 Hong Kong Obervatory**
719. **🌐 MetaWeather**
720. **🌐 ODWeather**
721. **🌐 OpenMeteo**
722. **🌐 openSenseMap**
723. **🌐 RainViewer**
724. **🌐 US Weather**
725. **🌐 weatherapi**

    """)

st.markdown("""
---
### How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run Home.py`

### About
This project is a showcase of the power of Streamlit and public APIs.
""")
