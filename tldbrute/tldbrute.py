
import argparse
import logging
import tldextract



#              ,----------------,              ,---------,
#         ,-----------------------,          ,"        ,"|
#       ,"                      ,"|        ,"        ,"  |
#      +-----------------------+  |      ,"        ,"    |
#      |  .-----------------.  |  |     +---------+      |
#      |  |                 |  |  |     | -==----'|      |
#      |  |  Sybil Scan!    |  |  |     |         |      |
#      |  |                 |  |  |/----|`---=    |      |
#      |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
#      |  |                 |  |  |  // |(((( [33]|    ,"
#      |  `-----------------'  |," .;'| |((((     |  ,"
#      +-----------------------+  ;;  | |         |,"    
#         /_)______________(_/  //'   | +---------+
#    ___________________________/___  `,
#   /  oooooooooooooooo  .o.  oooo /,   \,"-----------
#  / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
# /_==__==========__==_ooo__ooo=_/'   /___________,"
# `-----------------------------'


def generate(domain, tlds_name):
    tld_extract = tldextract.extract(domain)
    tld_domain = tld_extract.domain
    for names in tlds_name:
        print(tld_domain + "." + names)
    

def main():
    tld_names = ["0db", "0z", "1d", "1q7", "3dom", "4free", "4k", "4sale", "4youproof88", "8s", "abo", "aboutme", "aby", "ac", "aca", "academy", "accountant", "accountants", "actor", "addme", "adlt", "adult", "advisor", "ae.org", "afam", "africa", "afz", "agency", "ags", "agua", "ahoy", "ai", "airforce", "aj", "albums", "alto", "amg", "amigo", "amor", "ane", "annex", "aotearoa", "apartment", "apartments", "api", "app", "arbitrator", "army", "art", "artesanal", "articles", "artificial", "asia", "associates", "assurances", "atc", "ath", "attorney", "atwork", "auction", "audio", "augmented", "auto", "autos", "b2b", "baas", "baby", "badly", "bakes", "band", "bar", "bargains", "batch", "beach", "beauty", "beef", "beer", "bem", "berlin", "best", "bid", "bike", "bingo", "bio", "biometric", "bitcoinfund", "biz", "bizdata", "bizdev", "black", "blackfriday", "blockchaindapps", "blog", "blogging", "blue", "bmp", "boats", "bob", "bog", "bond", "boo", "booked", "boredapes", "boston", "boutique", "bqw", "br.com", "brand", "brewery", "brokers", "browsers", "btk9", "btt", "buddhist", "build", "builders", "business", "buyaflat", "buzz", "byn", "bz", "c", "c0m", "c4", "ca", "cab", "cabins", "cafe", "cam", "camera", "camp", "capital", "car", "cardcollector", "cards", "care", "careers", "cares", "cars", "casa", "cash", "casino", "catering", "catgirl", "causes", "cc", "center", "ceo", "cerrajero", "cfd", "ch", "charity", "chat", "cheap", "cheddar", "christmas", "church", "cism", "cita", "citizenship", "city", "ckq", "claims", "clc", "cleaning", "clic", "click", "client", "clients", "clinic", "cliq", "clothing", "cloud", "cloudbot", "club", "cm", "cm3", "cn", "cn.com", "cn3", "co", "co.bz", "co.com", "co.in", "co.uk", "co3", "coach", "codes", "codeschool", "coffee", "coffees", "coinnet", "college", "com", "com.au", "com.cn", "com.co", "com.de", "com.es", "com.mx", "com.pe", "com.ph", "com.se", "com.sg", "com.vc", "comic", "comics", "commerce", "communion", "community", "company", "complete", "computer", "computers", "concise", "condos", "conduct", "conductor", "conf", "connectors", "connoisseur", "construction", "consultancy", "consulting", "contact", "contractors", "cooking", "cool", "cork", "corporation", "country", "coupons", "courses", "crazy", "creations", "creativity", "creator", "credit", "creditcard", "crew", "cricket", "croatia", "cruises", "cryp", "cryptobets", "cryptogamer", "cryptoservice", "cuba", "cx", "cycle", "cymru", "cyou", "cyprus", "d5", "d8", "dais", "damn", "dan", "dance", "datamining", "date", "dating", "day", "daytrade", "dco", "de", "de.com", "de3", "deals", "dean", "debtless", "decent", "decentralize", "defi", "deficit", "degen", "degree", "delivery", "democrat", "den", "dental", "dentist", "desi", "design", "detour", "dev", "development", "dg", "dh", "diamonds", "dids", "diet", "digital", "digitalasset", "dilate", "direct", "directive", "directory", "discount", "discounts", "discussion", "diva", "dlt", "dly", "doctor", "dog", "doge", "dogecoin", "dojo", "dolls", "doma", "domains", "dookie", "douchebag", "down", "download", "downloads", "ds", "ducktape", "duration", "dvd", "dweb", "dweb3", "dy", "earth", "eathere", "eco", "economics", "economy", "edm", "education", "egame", "elect", "electronics", "elite", "email", "emj", "energy", "engaged", "engineer", "engineering", "enterprises", "ep", "eporn", "equipment", "ero", "es", "estate", "estates", "eternity", "etickets", "eu", "eu.com", "event", "events", "ewallet", "ewx", "exchange", "executive", "expert", "exposed", "express", "ext", "exu", "eyecare", "ez", "fail", "faith", "fak", "fam", "family", "fans", "faqs", "farm", "fashion", "fcb", "fd", "fe", "feedback", "feeling", "fej", "fellowship", "ffa", "fgz", "fia", "fiat2btc", "fiji", "film", "filters", "finance", "financial", "financialnews", "findme", "firstname", "fish", "fishing", "fit", "fitness", "fl3x", "flap", "flat", "flights", "florist", "flowers", "fm", "fmw", "follow", "foot", "football", "forall", "fore", "forsale", "forum", "foundation", "fr", "freebies", "fua", "fun", "fund", "fundraising", "furniture", "futbol", "fw", "fwd", "fyi", "gad", "gadget", "gallery", "game", "games", "garden", "gay", "gb.net", "gdl", "gdn", "ger", "gethigh", "getreal", "getwell", "gg", "gic", "gift", "gifts", "gin", "giveaways", "gives", "giving", "glass", "global", "gmbh", "gofor", "gold", "golf", "gon", "gonow", "goth", "gr.com", "grandmaster", "graphics", "gratis", "greatoffers", "green", "gripe", "group", "grow", "gruppen", "guey", "guidance", "guide", "guitars", "guru", "guz", "gvz", "gyc", "gzp", "hack", "hackathon", "hae", "hah", "hair", "haiti", "hamburg", "hardrive", "haus", "hb", "health", "healthcare", "heh", "hell", "help", "helpdesk", "hem", "hermanos", "hf", "hgo", "hill", "hiphop", "hire", "hits", "hockey", "hodlr", "holding", "holdings", "holiday", "holidayrental", "holidays", "homes", "hometown", "horny", "horse", "host", "hosting", "hotelguide", "house", "how", "hpp", "hsu", "hu.net", "hx", "i1", "ib", "ibn", "icu", "id", "ieh", "ifv", "ih", "ik", "ill", "iloveu", "immo", "immobilien", "in", "in.net", "inc", "income", "industries", "influencer", "info", "information", "inh", "ink", "innovator", "institute", "insure", "interest", "international", "intro", "investments", "iny", "io", "ioi", "ioo", "irish", "is", "island", "ism", "isthefuture", "italy", "iuh", "iurl", "iw", "ize", "ja", "january", "jao", "jeh", "jetzt", "jewelry", "jf", "job", "jok", "joker", "jov", "jp.net", "jpg", "jpgs", "jpn.com", "js", "jub", "juegos", "jugar", "jun", "jy", "kaufen", "kcx", "kennel", "keys", "kf", "kicks", "kids", "kim", "kinetic", "kip", "kitchen", "kiwi", "kj", "kl", "knight", "knowledge", "kq", "krd", "ks", "kv", "kyoto", "l33t", "la", "land", "lars", "lat", "lausanne", "law", "lawexpert", "lawoffice", "lawsuit", "lawyer", "lean", "lease", "legal", "legendary", "lgbt", "li", "life", "lighting", "likeapro", "limited", "limo", "lingo", "link", "live", "livestreaming", "ljb", "llc", "lli", "lnx", "lo", "loan", "loans", "logo", "lol", "london", "lord", "lov", "love", "lovesyou", "ltd", "ltda", "luxury", "lw", "lyf", "lz", "maestro", "magazine", "maison", "makeup", "management", "mansion", "market", "marketing", "mba", "me", "me.uk", "media", "mediator", "medico", "mee", "melbourne", "memorial", "men", "ment", "menu", "merc", "mev", "mex.com", "miami", "micro", "mined", "mission", "mke", "moar", "mobi", "moda", "moe", "mom", "mommy", "money", "monster", "montage", "mooning", "mortgage", "motherboard", "motorcycles", "movie", "mtl", "mvo", "mwallet", "mx", "mycard", "myco", "myo", "myproxy", "myurl", "nagoya", "nah", "name", "napavalley", "navy", "nearme", "neo", "nerdy", "net", "net.au", "net.cn", "net.pe", "net.ph", "net.vc", "network", "new", "news", "nftcartel", "nfts", "ngo", "nil", "ninja", "nl", "nod", "nom", "nom.es", "notes", "nouns", "npm", "nu", "nuk", "numb", "nxs", "nyc", "nym", "ob", "observer", "od", "oda", "oflinewallet", "often", "oh", "ohmy", "oin", "okinawa", "oncam", "one", "onewallet", "ong", "onl", "online", "onlinenews", "oo", "oof", "oot", "optimize", "oq", "orb", "org", "org.au", "org.cn", "org.es", "org.mx", "org.pe", "org.ph", "org.uk", "org.vc", "osaka", "oslo", "ot", "oun", "owbo", "p", "page", "paid", "pal", "paris", "partners", "parts", "party", "pave", "pdcst", "pe", "performer", "pest", "pgp", "ph", "photo", "photography", "photos", "pics", "picture", "pictures", "pier", "pink", "pix", "piz", "pizza", "place", "places", "plaza", "plumbing", "plus", "ply", "pockets", "poj", "poker", "policeman", "porn", "ppp", "praha", "premio", "premium", "presenter", "press", "prices", "pro", "prodazha", "productions", "profiles", "project", "properties", "property", "protection", "pub", "pui", "pun", "pv", "pw", "pz", "qd", "qf", "qg", "qh", "qk", "qn", "qo", "queens", "quest", "qum", "qy", "racing", "realty", "recipes", "red", "rehab", "reise", "reisen", "rekt", "remember", "rent", "rentals", "repair", "report", "republican", "researcher", "resources", "rest", "restaurant", "review", "reviews", "rh", "rican", "rip", "rl", "rn", "rocks", "rodeo", "rogan", "row", "rpgs", "rsvp", "ru.com", "rumor", "run", "runs", "rural", "russo", "rust", "ryukyu", "rz", "sa.com", "saas", "sale", "sales", "samples", "sarl", "sats", "say", "sbs", "school", "schooling", "schule", "science", "sds", "se.net", "secrets", "security", "semi", "services", "sex", "sexblog", "sexy", "sg", "sh", "sharing", "shark", "shiksha", "shizzle", "shoes", "shop", "shopping", "shoppingcart", "shortcut", "shot", "show", "shp", "sig", "simp", "simplicity", "singles", "site", "ski", "skin", "sniff", "so", "soccer", "social", "software", "solar", "solution", "solutions", "sos", "southafrican", "sox", "soy", "spac", "space", "specs", "squirtfiesta", "src", "ssl", "startup", "storage", "store", "stream", "streamer", "studio", "study", "style", "substack", "sucks", "supplies", "supply", "support", "supreme", "surf", "surgery", "sus", "swapz", "sydney", "systems", "tao", "tar", "tattoo", "tax", "taxfree", "taxi", "team", "tech", "techblog", "technology", "teck", "teenager", "teepee", "tefi", "tel", "tennis", "ter", "theater", "theatre", "thenerd", "tickets", "tienda", "tips", "tires", "tni", "to", "today", "token", "tokyo", "tools", "top", "tours", "town", "toys", "trade", "trader", "training", "trans", "travel", "trekking", "tricks", "troll", "tube", "tuber", "turtles", "tutorial", "tv", "tx", "u2", "ud", "ue", "uf", "uge", "uk", "uk.com", "uk.net", "uk3", "ultimate", "umo", "underground", "underworld", "unit", "universe", "university", "unlock", "uno", "us", "us.com", "us.org", "us3", "use", "uui", "uzr", "vacations", "valley", "vase", "vc", "vegas", "ventures", "vet", "viajes", "video", "vie", "viewer", "villas", "vin", "vip", "vision", "visit", "vj", "vlog", "vodka", "voice", "vote", "voting", "voto", "voyage", "vq", "vuo", "w33d", "w3b", "w3n", "w8", "wales", "wasabi", "watch", "wave", "wc", "we3", "web4", "webartist", "webcam", "webdesigner", "website", "websites", "wedding", "wh", "whitepaper", "wiki", "win", "wine", "wj", "wl", "won", "work", "works", "world", "worldtour", "wq", "wr", "ws", "wt", "wtf", "x00m", "x2", "xa", "xb", "xc", "xcam", "xf", "xg", "xi", "xk", "xn--3ds443g", "xn--5o8h", "xn--6ca", "xn--6frz82g", "xn--dei", "xn--dp8h", "xn--e77hhb", "xn--g6h", "xn--pei", "xn--rci", "xq", "xr", "xxx", "xxxx", "xyz", "yachts", "yb", "yd", "year", "yh", "yj", "yo", "yoga", "yokohama", "yol", "yolo", "yq", "yummy", "yx", "yzx", "za.com", "zc", "zen", "zh", ".0db", "0z", "1", "1d", "1q7", "3dom", "4free", "4k", "4sale", "4youproof88", "8s", "abo", "aboutme", "aby", "ac", "aca", "academy", "accountant", "accountants", "actor", "addme", "adlt", "adult", "advisor", "ae.org", "afam", "africa", "afz", "agency", "ags", "agua", "ahoy", "ai", "airforce", "aj", "albums", "alto", "amg", "amigo", "amor", "ane", "annex", "aotearoa", "apartment", "apartments", "api", "app", "arbitrator", "army", "art", "artesanal", "articles", "artificial", "asia", "associates", "assurances", "atc", "ath", "attorney", "atwork", "auction", "audio", "augmented", "auto", "autos", "b2b", "baas", "baby", "badly", "bakes", "band", "bar", "bargains", "batch", "beach", "beauty", "beef", "beer", "bem", "berlin", "best", "bid", "bike", "bingo", "bio", "biometric", "bitcoinfund", "biz", "bizdata", "bizdev", "black", "blackfriday", "blockchaindapps", "blog", "blogging", "blue", "bmp", "boats", "bob", "bog", "bond", "boo", "booked", "boredapes", "boston", "boutique", "bqw", "br.com", "brand", "brewery", "brokers", "browsers", "btk9", "btt", "buddhist", "build", "builders", "business", "buyaflat", "buzz", "byn", "bz", "c", "c0m", "c4", "ca", "cab", "cabins", "cafe", "cam", "camera", "camp", "capital", "car", "cardcollector", "cards", "care", "careers", "cares", "cars", "casa", "cash", "casino", "catering", "catgirl", "causes", "cc", "center", "ceo", "cerrajero", "cfd", "ch", "charity", "chat", "cheap", "cheddar", "christmas", "church", "cism", "cita", "citizenship", "city", "ckq", "claims", "clc", "cleaning", "clic", "click", "client", "clients", "clinic", "cliq", "clothing", "cloud", "cloudbot", "club", "cm", "cm3", "cn", "cn.com", "cn3", "co", "co.bz", "co.com", "co.in", "co.uk", "co3", "coach", "codes", "codeschool", "coffee", "coffees", "coinnet", "college", "com", "com.au", "com.cn", "com.co", "com.de", "com.es", "com.mx", "com.pe", "com.ph", "com.se", "com.sg", "com.vc", "comic", "comics", "commerce", "communion", "community", "company", "complete", "computer", "computers", "concise", "condos", "conduct", "conductor", "conf", "connectors", "connoisseur", "construction", "consultancy", "consulting", "contact", "contractors", "cooking", "cool", "cork", "corporation", "country", "coupons", "courses", "crazy", "creations", "creativity", "creator", "credit", "creditcard", "crew", "cricket", "croatia", "cruises", "cryp", "cryptobets", "cryptogamer", "cryptoservice", "cuba", "cx", "cycle", "cymru", "cyou", "cyprus", "d5", "d8", "dais", "damn", "dan", "dance", "datamining", "date", "dating", "day", "daytrade", "dco", "de", "de.com", "de3", "deals", "dean", "debtless", "decent", "decentralize", "defi", "deficit", "degen", "degree", "delivery", "democrat", "den", "dental", "dentist", "desi", "design", "detour", "dev", "development", "dg", "dh", "diamonds", "dids", "diet", "digital", "digitalasset", "dilate", "direct", "directive", "directory", "discount", "discounts", "discussion", "diva", "dlt", "dly", "doctor", "dog", "doge", "dogecoin", "dojo", "dolls", "doma", "domains", "dookie", "douchebag", "down", "download", "downloads", "ds", "ducktape", "duration", "dvd", "dweb", "dweb3", "dy", "earth", "eathere", "eco", "economics", "economy", "edm", "education", "egame", "elect", "electronics", "elite", "email", "emj", "energy", "engaged", "engineer", "engineering", "enterprises", "ep", "eporn", "equipment", "ero", "es", "estate", "estates", "eternity", "etickets", "eu", "eu.com", "event", "events", "ewallet", "ewx", "exchange", "executive", "expert", "exposed", "express", "ext", "exu", "eyecare", "ez", "fail", "faith", "fak", "fam", "family", "fans", "faqs", "farm", "fashion", "fcb", "fd", "fe", "feedback", "feeling", "fej", "fellowship", "ffa", "fgz", "fia", "fiat2btc", "fiji", "film", "filters", "finance", "financial", "financialnews", "findme", "firstname", "fish", "fishing", "fit", "fitness", "fl3x", "flap", "flat", "flights", "florist", "flowers", "fm", "fmw", "follow", "foot", "football", "forall", "fore", "forsale", "forum", "foundation", "fr", "freebies", "fua", "fun", "fund", "fundraising", "furniture", "futbol", "fw", "fwd", "fyi", "gad", "gadget", "gallery", "game", "games", "garden", "gay", "gb.net", "gdl", "gdn", "ger", "gethigh", "getreal", "getwell", "gg", "gic", "gift", "gifts", "gin", "giveaways", "gives", "giving", "glass", "global", "gmbh", "gofor", "gold", "golf", "gon", "gonow", "goth", "gr.com", "grandmaster", "graphics", "gratis", "greatoffers", "green", "gripe", "group", "grow", "gruppen", "guey", "guidance", "guide", "guitars", "guru", "guz", "gvz", "gyc", "gzp", "hack", "hackathon", "hae", "hah", "hair", "haiti", "hamburg", "hardrive", "haus", "hb", "health", "healthcare", "heh", "hell", "help", "helpdesk", "hem", "hermanos", "hf", "hgo", "hill", "hiphop", "hire", "hits", "hockey", "hodlr", "holding", "holdings", "holiday", "holidayrental", "holidays", "homes", "hometown", "horny", "horse", "host", "hosting", "hotelguide", "house", "how", "hpp", "hsu", "hu.net", "hx", "i1", "ib", "ibn", "icu", "id", "ieh", "ifv", "ih", "ik", "ill", "iloveu", "immo", "immobilien", "in", "in.net", "inc", "income", "industries", "influencer", "info", "information", "inh", "ink", "innovator", "institute", "insure", "interest", "international", "intro", "investments", "iny", "io", "ioi", "ioo", "irish", "is", "island", "ism", "isthefuture", "italy", "iuh", "iurl", "iw", "ize", "ja", "january", "jao", "jeh", "jetzt", "jewelry", "jf", "job", "jok", "joker", "jov", "jp.net", "jpg", "jpgs", "jpn.com", "js", "jub", "juegos", "jugar", "jun", "jy", "kaufen", "kcx", "kennel", "keys", "kf", "kicks", "kids", "kim", "kinetic", "kip", "kitchen", "kiwi", "kj", "kl", "knight", "knowledge", "kq", "krd", "ks", "kv", "kyoto", "l33t", "la", "land", "lars", "lat", "lausanne", "law", "lawexpert", "lawoffice", "lawsuit", "lawyer", "lean", "lease", "legal", "legendary", "lgbt", "li", "life", "lighting", "likeapro", "limited", "limo", "lingo", "link", "live", "livestreaming", "ljb", "llc", "lli", "lnx", "lo", "loan", "loans", "logo", "lol", "london", "lord", "lov", "love", "lovesyou", "ltd", "ltda", "luxury", "lw", "lyf", "lz", "maestro", "magazine", "maison", "makeup", "management", "mansion", "market", "marketing", "mba", "me", "me.uk", "media", "mediator", "medico", "mee", "melbourne", "memorial", "men", "ment", "menu", "merc", "mev", "mex.com", "miami", "micro", "mined", "mission", "mke", "moar", "mobi", "moda", "moe", "mom", "mommy", "money", "monster", "montage", "mooning", "mortgage", "motherboard", "motorcycles", "movie", "mtl", "mvo", "mwallet", "mx", "mycard", "myco", "myo", "myproxy", "myurl", "nagoya", "nah", "name", "napavalley", "navy", "nearme", "neo", "nerdy", "net", "net.au", "net.cn", "net.pe", "net.ph", "net.vc", "network", "new", "news", "nftcartel", "nfts", "ngo", "nil", "ninja", "nl", "nod", "nom", "nom.es", "notes", "nouns", "npm", "nu", "nuk", "numb", "nxs", "nyc", "nym", "ob", "observer", "od", "oda", "oflinewallet", "often", "oh", "ohmy", "oin", "okinawa", "oncam", "one", "onewallet", "ong", "onl", "online", "onlinenews", "oo", "oof", "oot", "optimize", "oq", "orb", "org", "org.au", "org.cn", "org.es", "org.mx", "org.pe", "org.ph", "org.uk", "org.vc", "osaka", "oslo", "ot", "oun", "owbo", "p", "page", "paid", "pal", "paris", "partners", "parts", "party", "pave", "pdcst", "pe", "performer", "pest", "pgp", "ph", "photo", "photography", "photos", "pics", "picture", "pictures", "pier", "pink", "pix", "piz", "pizza", "place", "places", "plaza", "plumbing", "plus", "ply", "pockets", "poj", "poker", "policeman", "porn", "ppp", "praha", "premio", "premium", "presenter", "press", "prices", "pro", "prodazha", "productions", "profiles", "project", "properties", "property", "protection", "pub", "pui", "pun", "pv", "pw", "pz", "qd", "qf", "qg", "qh", "qk", "qn", "qo", "queens", "quest", "qum", "qy", "racing", "realty", "recipes", "red", "rehab", "reise", "reisen", "rekt", "remember", "rent", "rentals", "repair", "report", "republican", "researcher", "resources", "rest", "restaurant", "review", "reviews", "rh", "rican", "rip", "rl", "rn", "rocks", "rodeo", "rogan", "row", "rpgs", "rsvp", "ru.com", "rumor", "run", "runs", "rural", "russo", "rust", "ryukyu", "rz", "sa.com", "saas", "sale", "sales", "samples", "sarl", "sats", "say", "sbs", "school", "schooling", "schule", "science", "sds", "se.net", "secrets", "security", "semi", "services", "sex", "sexblog", "sexy", "sg", "sh", "sharing", "shark", "shiksha", "shizzle", "shoes", "shop", "shopping", "shoppingcart", "shortcut", "shot", "show", "shp", "sig", "simp", "simplicity", "singles", "site", "ski", "skin", "sniff", "so", "soccer", "social", "software", "solar", "solution", "solutions", "sos", "southafrican", "sox", "soy", "spac", "space", "specs", "squirtfiesta", "src", "ssl", "startup", "storage", "store", "stream", "streamer", "studio", "study", "style", "substack", "sucks", "supplies", "supply", "support", "supreme", "surf", "surgery", "sus", "swapz", "sydney", "systems", "tao", "tar", "tattoo", "tax", "taxfree", "taxi", "team", "tech", "techblog", "technology", "teck", "teenager", "teepee", "tefi", "tel", "tennis", "ter", "theater", "theatre", "thenerd", "tickets", "tienda", "tips", "tires", "tni", "to", "today", "token", "tokyo", "tools", "top", "tours", "town", "toys", "trade", "trader", "training", "trans", "travel", "trekking", "tricks", "troll", "tube", "tuber", "turtles", "tutorial", "tv", "tx", "u2", "ud", "ue", "uf", "uge", "uk", "uk.com", "uk.net", "uk3", "ultimate", "umo", "underground", "underworld", "unit", "universe", "university", "unlock", "uno", "us", "us.com", "us.org", "us3", "use", "uui", "uzr", "vacations", "valley", "vase", "vc", "vegas", "ventures", "vet", "viajes", "video", "vie", "viewer", "villas", "vin", "vip", "vision", "visit", "vj", "vlog", "vodka", "voice", "vote", "voting", "voto", "voyage", "vq", "vuo", "w33d", "w3b", "w3n", "w8", "wales", "wasabi", "watch", "wave", "wc", "we3", "web4", "webartist", "webcam", "webdesigner", "website", "websites", "wedding", "wh", "whitepaper", "wiki", "win", "wine", "wj", "wl", "won", "work", "works", "world", "worldtour", "wq", "wr", "ws", "wt", "wtf", "x00m", "x2", "xa", "xb", "xc", "xcam", "xf", "xg", "xi", "xk", "xn--3ds443g", "xn--5o8h", "xn--6ca", "xn--6frz82g", "xn--dei", "xn--dp8h", "xn--e77hhb", "xn--g6h", "xn--pei", "xn--rci", "xq", "xr", "xxx", "xxxx", "xyz", "yachts", "yb", "yd", "year", "yh", "yj", "yo", "yoga", "yokohama", "yol", "yolo", "yq", "yummy", "yx", "yzx", "za.com", "zc", "zen", "zh", "zone", "zoy", "zp", "zs", "zug", "zx", "zy", "zone", "zoy", "zp", "zs", "zug", "zx", "zy"]
    

    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.info("""\u001b[33;1m

 ________   ___  __            __     
/_  __/ /  / _ \/ /  ______ __/ /____ 
 / / / /__/ // / _ \/ __/ // / __/ -_)
/_/ /____/____/_.__/_/  \_,_/\__/\__/ 
                                      
                    
                \u001b[36;1m - by Sybil Scan Research <research@sybilscan.com>\u001b[0m 
    """)
    parser = argparse.ArgumentParser(description='TLDbrute : A simple utility to generate domain names with all possible TLDs')
    parser.add_argument('-d','--domain' , help = 'Domain name to generate all TLD variations')
    parser.add_argument('-l', '--list', help = 'List of domains to generate all TLD variations')
    args = parser.parse_args()

    if args.list:
        with open(args.list) as f:
            content = f.readlines()
        domains = [x.strip() for x in content]
        print(domains)
        for domain in domains:
            generate(domain, tld_names)
        

    if args.domain:
        generate(args.domain, tld_names)
