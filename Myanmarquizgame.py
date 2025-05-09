import json
import random
import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7857608827:AAG8I7WNivIQLiI1qs5kL-xGuxSzmdXPlxU"

questions = [
{
      "question": "မြန်မာပြည်၏ပထမဆုံးသောအစိုးရသည် ဘယ်နှစ်တွင် ဖွဲ့စည်းခဲ့သနည်း။",
      "options": ["၁၉၄၈", "၁၉၄၅", "၁၉၃၅", "၁၉၂၀"],
      "correct": "၁၉၄၈"
   },
   {
      "question": "မြန်မာပြည်ရှိ မြောက်ပိုင်းနိုင်ငံကြီးတစ်ခုရဲ့နာမည်မှာ ဘာလဲ။",
      "options": ["ချင်းပြည်", "ကချင်ပြည်", "ရှမ်းပြည်", "ကရင်ပြည်"],
      "correct": "ကချင်ပြည်"
   },
   {
      "question": "မြန်မာနိုင်ငံအတွက်ပထမဆုံးထုတ်လုပ်ခဲ့သောရိုးရာကြော်ငြာကို ဘယ်နှစ်တွင်ထုတ်ပြန်ခဲ့သနည်း။",
      "options": ["၁၉၂၀", "၁၉၃၀", "၁၉၄၀", "၁၉၀၀"],
      "correct": "၁၉၂၀"
   },
   {
      "question": "မြန်မာအမျိုးသားဂိမ်းချိတ်ဆွဲမှုအကြီးဆုံးဂိမ်းကျွမ်းသူအမည်ကဘာလဲ။",
      "options": ["မောင်မောင်", "လင်းခိုင်", "ကြွယ်လက်", "သန်းထွေး"],
      "correct": "မောင်မောင်"
   },
   {
      "question": "အခေ့လေးတွင် မြန်မာ့မတ်ဆန်းရဲ့တည်နေရာမှာ ထိပ်တန်းအားဖြင့်ဆောင်ရွက်သည့်ရပ်တည်ဘယ်နေရာတွင်ရှိသလဲ။",
      "options": ["နန်းတော်ကျေး", "လင်းကျိုက်တည်", "ယုံယုံ", "ဘတ်ပန်းစရာ"],
      "correct": "လင်းကျိုက်တည်"
   },
   {
      "question": "မြန်မာပြည်အခြေအနေဖြင့် ဘုရင်တစ်လျှောက်လုံးကို ကမ္ဘာပေါ်တွင်အကျုံးကျော်ခဲ့သည့်လူတစ်ဦးရဲ့အမည် ဘာလဲ။",
      "options": ["ဦးမောင်ဝေ", "အောင်မြင့်", "မြင့်ကွေး", "ထွန်းလင်း"],
      "correct": "မြင့်ကွေး"
   },
   {
      "question": "မြန်မာနိုင်ငံ၏ ပထမဆုံးတင်သွင်းသည့် စီးပွားရေးသင်တန်းစာသင်ပုဂ္ဂိုလ်အမည် ဘာလဲ။",
      "options": ["သန်းထွေး", "ဒေါ်ခင်ကျော်", "အောင်ဆန်း", "သဿသီး"],
      "correct": "ဒေါ်ခင်ကျော်"
   },
   {
      "question": "မြန်မာနိုင်ငံ၏အမြင့်ဆုံးတောင်ဖြစ်သော တောင်အမည်မှာ ဘာလဲ။",
      "options": ["မထကတောင်", "ကဲလသီတောင်", "ဟခါဘူမတောင်", "ချောင်းသီတောင်"],
      "correct": "မထကတောင်"
   },
   {
      "question": "မြန်မာနိုင်ငံ၏အကြီးဆုံးကန်မှာ ဘာအမည်ရှိသနည်း။",
      "options": ["အင်းလေးကန်", "အင်းတော်ကန်", "ငပလေးကန်", "မယ်ဇလွန်ကန်"],
      "correct": "အင်းလေးကန်"
   },
   {
      "question": "မြန်မာပြည်တွင် အကြီးဆုံးကျွန်းအမည်ဘာလဲ။",
      "options": ["ကမ္ဘောဇကျွန်း", "ပင်လယ်ကြီးကျွန်း", "မြောက်ဥက္ကဋ္ဌကျွန်း", "မောင်းမလေးကျွန်း"],
      "correct": "မောင်းမလေးကျွန်း"
   },
   {
      "question": "မြန်မာ့နာမည်ကြီးသံတော်ဆင်၏အရောင်များမှာ ဘာလဲ။",
      "options": ["အနီ၊ အဖြူ၊ အစိမ်း", "အနီ၊ အမဲ၊ အဝါ", "အနီ၊ အဖြူ၊ အပြာ", "အဝါ၊ အစိမ်း၊ အနီ"],
      "correct": "အနီ၊ အဖြူ၊ အစိမ်း"
   },
   {
      "question": "မြန်မာနိုင်ငံ၏ရေကြီးဆုံးမြစ်သည် ဘာမြစ်လဲ။",
      "options": ["ဧရာဝတီမြစ်", "ပင်လယ်ကြီး", "မန်ခန်းမြစ်", "လကှမ်မြစ်"],
      "correct": "ဧရာဝတီမြစ်"
   },
   {
      "question": "မြန်မာနိုင်ငံ၏ပထမဆုံးတက္ကသိုလ်အမည်မှာ ဘာလဲ။",
      "options": ["တောင်ငူတက္ကသိုလ်", "ရန်ကုန်တက္ကသိုလ်", "မဟာမြတ်တက္ကသိုလ်", "ပုဂံတက္ကသိုလ်"],
      "correct": "ရန်ကုန်တက္ကသိုလ်"
   },

    {
        "question": "မြန်မာနိုင်ငံ၏အနောက်ဖက်အနီးအနားတွင်တည်ရှိသောနိုင်ငံမှာ ဘယ်နိုင်ငံလဲ။",
        "options": ["အိန္ဒိယ", "ဧရာဝတီ", "လာအို", "ထိုင်း"],
        "correct": "အိန္ဒိယ"
    },
    {
        "question": "ပုဂံအကြီးဆုံးဘုရားတည်ရှိရာ မြို့တော်၏အမည်ကဘာလဲ။",
        "options": ["ပုဂံ", "မင်းစကြာ", "ရခိုင်", "တောင်ငူ"],
        "correct": "ပုဂံ"
    },
    {
        "question": "မြန်မာ့သမိုင်းတွင် 'အိပ်မက်တောင်' အဖြစ်ကျော်ကြားသည့် တောင်မှာ ဘယ်တောင်လဲ။",
        "options": ["မတကတောင်", "ဘုရင်သီတင်း", "ထိုင်းတောင်", "အလွယ်တံတား"],
        "correct": "မတကတောင်"
    },
    {
        "question": "ဒုတိယမြန်မာစစ်တွင် ဗြိတိသျှများနှင့် မြန်မာတို့၏ စစ်ပွဲကို ကွဲလားခဲ့သောသူက ဘယ်သူလဲ။",
        "options": ["ဗိုလ်ချုပ်အောင်ဆန်း", "အောင်ဆန်းဗိုလ်ချုပ်", "သီပေါ", "မင်းဂို"],
        "correct": "ဗိုလ်ချုပ်အောင်ဆန်း"
    },
    {
        "question": "တောမြင်းပွင့်ပွန်းသည် မြန်မာပေါ့လေး၏ အဓိကအစားအစာဖြစ်တဲ့ပုံတွင် ဘယ်အရာတစ်ခုဖြစ်သည်။",
        "options": ["ရှုံးချိုး", "ရက်သတ္တိ", "ပုလဲသီး", "ကြက်သွန်ဖြူ"],
        "correct": "ရက်သတ္တိ"
    },
    {
        "question": "ဗမာ့လက်နက်စနစ်ကို တီထွင်ခဲ့သည့် မြန်မာမင်းသည် ဘယ်သူလဲ။",
        "options": ["လက်ခွေမင်း", "မင်းတိုင်", "မင်းသန်း", "ဘုရင်သူနောင်"],
        "correct": "မင်းတိုင်"
    },
    {
        "question": "မြန်မာနိုင်ငံ၏အရှေ့ဖက်အနီးအနားတွင်တည်ရှိသောနိုင်ငံမှာ ဘယ်နိုင်ငံလဲ။",
        "options": ["ဘင်္ဂလားဒေ့ရှ်", "ထိုင်း", "တရုတ်", "လာအို"],
        "correct": "ထိုင်း"
    },
    {
        "question": "ဒုတိယနိုင်ငံရေးအဖွဲ့ဖြစ်သော ဗမာ့လွတ်မြောက်ရေးအဖွဲ့ (BIA) ကို မည်သည့်နှစ်တွင် ဖွဲ့စည်းခဲ့သနည်း။",
        "options": ["၁၉၄၁", "၁၉၄၂", "၁၉၄၈", "၁၉၃၀"],
        "correct": "၁၉၄၂"
    },
    {
        "question": "ပုဂံခေတ်အတွင်း တည်ဆောက်ခဲ့သော နာမည်ကြီးဘုရားတစ်ခုမှာ ဘာလဲ။",
        "options": ["အနန္ဒာဘုရား", "ရွှေတိဂုံစေတီ", "ဘုရားကြီး", "ဆယ်ကြီးဘုရား"],
        "correct": "အနန္ဒာဘုရား"
    },
    {
        "question": "ဗြိတိသျှအင်ပါယာနှင့် သမိုင်းအရေးကြီးစစ်ပွဲတစ်ခုဖြစ်သည့် တတိယအင်္ဂလိပ်မြန်မာစစ်သည် မည်သည့်နှစ်တွင် ဖြစ်ပွားသနည်း။",
        "options": ["၁၈၈၅", "၁၈၅၂", "၁၈၂၄", "၁၉၀၁"],
        "correct": "၁၈၈၅"
    },
    {
        "question": "ဦးသိန်းစိန်သည် မည်သည့်အရာအတွက်နာမည်ကြီးသနည်း။",
        "options": ["သမ္မတ", "တပ်မတော်ချုပ်", "လွှတ်တော်ဥက္ကဋ္ဌ", "ဝန်ကြီးချုပ်"],
        "correct": "သမ္မတ"
    },
    {
        "question": "မြန်မာနိုင်ငံ၏အမြင့်ဆုံးတောင်သည် မထကတောင်ဖြစ်သည်။ ၎င်းတောင်၏အမြင့်မှာ ဘယ်လောက်လဲ။",
        "options": ["၁၃,၅၈၅ ပေ", "၁၉,၂၉၆ ပေ", "၁၅,၂၅၀ ပေ", "၁၇,၃၈၉ ပေ"],
        "correct": "၁၉,၂၉၆ ပေ"
    },
    {
        "question": "ပဉ္စမမြန်မာစာအုပ်၏စာရေးသူမှာ ဘယ်သူလဲ။",
        "options": ["ပေါင်စည်", "သန်းမောင်", "အောင်သိန်း", "စန်းသော်"],
        "correct": "သန်းမောင်"
    },
    {
        "question": "မင်းထက်စံဘုရင်သည် မည်သည့်ဘုရင့်နောင်ဖြစ်သနည်း။",
        "options": ["ပုဂံဘုရင်", "အင်းဝဘုရင်", "ကုန်းဘုရင်", "မင်းတွင်းဘုရင်"],
        "correct": "ကုန်းဘုရင်"
    },
    {
        "question": "မြန်မာ့သမိုင်းထဲမှ တော်ဝင်အမျိုးသမီးကြီးတစ်ဦးဖြစ်သော မုဆိုးမင်းမယ်သည် ဘယ်ဘုရင်၏မယားလဲ။",
        "options": ["နရေနောင်", "အနော်ရထာ", "သီပေါ", "စကြာ"],
        "correct": "အနော်ရထာ"
    },
    {
        "question": "မုံရွာမြို့သည် မည်သည့်တိုင်းဒေသကြီးတွင် တည်ရှိသနည်း။",
        "options": ["စစ်ကိုင်း", "မန္တလေး", "မကွေး", "ဧရာဝတီ"],
        "correct": "စစ်ကိုင်း"
    },
    {
        "question": "မြန်မာ့ပထမဆုံးဝန်ကြီးချုပ်ဖြစ်သူ ဦးနု သည် မည်သည့်ပါတီမှ ဖြစ်သနည်း။",
        "options": ["AFPFL", "NLD", "SNLD", "USDP"],
        "correct": "AFPFL"
    },
    {
        "question": "ရွှေတိဂုံစေတီတော်သည် မည်သည့်မြို့တွင် တည်ရှိသည်။",
        "options": ["မန္တလေး", "နေပြည်တော်", "ရန်ကုန်", "ပုသိမ်"],
        "correct": "ရန်ကုန်"
    },
    {
        "question": "ဗိုလ်ချုပ်အောင်ဆန်း၏ မိခင်အမည်မှာ ဘယ်သူလဲ။",
        "options": ["ဒေါ်အိ", "ဒေါ်စု", "ဒေါ်ခင်ကြည်", "ဒေါ်ခင်သန်း"],
        "correct": "ဒေါ်ခင်ကြည်"
    },
    {
        "question": "ပုဂံမြို့ကို တည်ထောင်ခဲ့သောဘုရင်မှာ ဘယ်သူလဲ။",
        "options": ["ဘုရင်အနုရုဒ္ဓ", "မင်းစကြာ", "သူနောင်", "ဓမ္မယဇ"],
        "correct": "မင်းစကြာ"
    },
    {
        "question": "မြန်မာနိုင်ငံတွင် အကြီးဆုံးကျွန်းမှာ ဘာအမည်ရှိသနည်း။",
        "options": ["ကမ္ဘောဇကျွန်း", "ဗြာအင်းကျွန်း", "မောင်းမလေးကျွန်း", "ပင်လယ်ကြီးကျွန်း"],
        "correct": "မောင်းမလေးကျွန်း"
    },
    {
        "question": "ဦးအောင်ဆန်း၏တော်လှန်ရေးလုပ်ငန်းတွင်ပါဝင်ခဲ့သော နာမည်ကြီးအမျိုးသားတစ်ဦးမှာ ဘယ်သူလဲ။",
        "options": ["ဦးဘုန်းနိုင်", "ဦးနု", "ဦးကျော်ဟုန်", "ဒေါက်တာအေး"],
        "correct": "ဒေါက်တာအေး"
    },
    {
        "question": "မြန်မာ့သမိုင်းတွင် နာမည်ကြီးသော ရှမ်းဘုရင်မှာ ဘယ်သူလဲ။",
        "options": ["စော်ဘွားဖုန်းနောင်", "စော်ဘွားဖုန်းသုံး", "စော်ဘွားစိန်", "စော်ဘွားငယ်"],
        "correct": "စော်ဘွားဖုန်းနောင်"
    },
    {
        "question": "အင်းဝမြို့သည် မည်သည့်ခေတ်တွင် မြို့တော်အဖြစ်သုံးခဲ့သနည်း။",
        "options": ["ကိုနဘောခေတ်", "တောင်ငူခေတ်", "အင်းဝခေတ်", "မင်းတွင်းခေတ်"],
        "correct": "အင်းဝခေတ်"
    },
    {
        "question": "အမျိုးသားသံတော်ဆင်သည် မြန်မာပြည်သူအတွက် ဘာကိုကိုယ်စားပြုသနည်း။",
        "options": ["ငြိမ်းချမ်းရေး", "အာဏာအုပ်ချုပ်မှု", "သမ္မတ", "အမျိုးသားရေး"],
        "correct": "အမျိုးသားရေး"
    },
    {
        "question": "မြန်မာ့နောက်ဆုံးဘုရင်ဖြစ်သူမှာ ဘယ်သူလဲ။",
        "options": ["မင်းဒင်မင်း", "တောင်ဦးမင်း", "သူနောင်မင်း", "သီပေါမင်း"],
        "correct": "သီပေါမင်း"
    },
    {
        "question": "မြန်မာ့သမိုင်းတွင် 'အမျိုးသားဘိုးဘွား' ဟုခေါ်သောသူမှာ ဘယ်သူလဲ။",
        "options": ["ဗိုလ်ချုပ်အောင်ဆန်း", "သန်းထွေး", "ဦးနု", "ဒေါက်တာအေး"],
        "correct": "ဗိုလ်ချုပ်အောင်ဆန်း"
    },
    {
        "question": "ပုဂံခေတ်၏ နာမည်ကြီးဘုရင်တစ်ဦးမှာ ဘယ်သူလဲ။",
        "options": ["အနော်ရထာ", "ကျော်ဇော", "အနော်ဘုရင်", "တိုးမင်း"],
        "correct": "အနော်ရထာ"
    },
    {
        "question": "မြန်မာနိုင်ငံတွင်အကြီးဆုံးကန်မှာ ဘယ်ကန်လဲ။",
        "options": ["အင်းလေးကန်", "ငပလေးကန်", "အင်းတော်ကန်", "မယ်ဇလွန်ကန်"],
        "correct": "အင်းလေးကန်"
    },
    {
        "question": "အမျိုးသားသမိုင်းဂုဏ်ထူးဆောင်အမျိုးသမီးတစ်ဦးမှာ ဘယ်သူလဲ။",
        "options": ["ဒေါ်အောင်ဆန်းစုကြည်", "ဒေါ်သော်တာ", "ဒေါ်ဦးမြင့်မြတ်", "ဒေါ်ချစ်ချစ်ခင်"],
        "correct": "ဒေါ်အောင်ဆန်းစုကြည်"
    },
    {
        "question": "မြန်မာ့အကအနုပညာမှာ နာမည်ကြီးသောအမျိုးသားအကသည်ဘယ်အကလဲ။",
        "options": ["လုံချည်အက", "ရိုးရာအက", "အမည်မသိအက", "စင်မြင့်အက"],
        "correct": "လုံချည်အက"
    },
    {
        "question": "မြန်မာ့ရုပ်ရှင်ထူးချွန်ဆုကို စတင်ချီးမြှင့်ခဲ့သည့်နှစ်မှာ ဘယ်နှစ်လဲ။",
        "options": ["၁၉၅၂", "၁၉၄၈", "၁၉၆၄", "၁၉၇၀"],
        "correct": "၁၉၅၂"
    },
    {
        "question": "တောင်သူလယ်သမားနေ့ကို မြန်မာနိုင်ငံတွင် မည်သည့်နေ့တွင် ကျင်းပသည်။",
        "options": ["မတ် ၂", "ဖေဖော်ဝါရီ ၁၂", "ဇူလိုင် ၁၉", "ဇန်နဝါရီ ၄"],
        "correct": "မတ် ၂"
    },
    {
        "question": "မြန်မာ့ရုပ်ရှင်တော်ဝင်မင်းသမီးတစ်ဦးမှာ ဘယ်သူလဲ။",
        "options": ["မယ်မယ်ချစ်", "မေမေဝင်း", "ဝိုင်းဝိုင်း", "ခင်သွေးခိုင်"],
        "correct": "မေမေဝင်း"
    },
    {
        "question": "တောင်ငူမြို့ကို တည်ထောင်သူ ဘုရင်မှာ ဘယ်သူလဲ။",
        "options": ["ဘုရင့်နောင်", "အနော်ရထာ", "နောင်ဒုက္ခ", "သစၥာမင်း"],
        "correct": "ဘုရင့်နောင်"
    },
    {
        "question": "မြန်မာ့စာပေဆုတစ်ခုဖြစ်သော 'စိန်တံဆိပ်ဆု' ကို မည်သည့်အဖွဲ့အစည်းမှချီးမြှင့်သနည်း။",
        "options": ["ပြည်ထောင်စုလွှတ်တော်", "အမျိုးသားစာပေကောင်စီ", "ပညာရေးဝန်ကြီးဌာန", "စာပေအသင်းကြီး"],
        "correct": "အမျိုးသားစာပေကောင်စီ"
    },
{
        "question": "မြန်မာနိုင်ငံကို ဘရိတိသျှများ စတင်ကျူးကျော်ခဲ့သောနှစ်မှာ ဘယ်နှနှစ်လဲ။",
        "options": ["၁၈၈၅", "၁၈၂၄", "၁၉၄၈", "၁၉၂၀"],
        "correct": "၁၈၂၄"
    },
    {
    "question": "ဗိုလ်ချုပ်အောင်ဆန်းဖွဲ့စည်းခဲ့သော တပ်ဖွဲ့မှာ ဘာအမည်ရှိသနည်း။",
    "options": ["အောင်သံဝေဖွဲ့", "မြန်မာအမျိုးသားတပ်မတော်", "ဗမာ့တပ်မတော်", "အန်အဲဖ်အဲဖ်"],
    "correct": "အန်အဲဖ်အဲဖ်"
},
{
    "question": "မြန်မာ့ပထမဆုံးတက္ကသိုလ်ကို မည်သည့်နှစ်တွင် တည်ထောင်ခဲ့သနည်း။",
    "options": ["၁၉၂၀", "၁၈၈၅", "၁၉၃၇", "၁၉၄၈"],
    "correct": "၁၉၂၀"
},
{
    "question": "ပထမအင်္ဂလိပ်မြန်မာစစ်ဖြစ်ပွားခဲ့သည့်နှစ်မှာ ဘယ်နှနှစ်လဲ။",
    "options": ["၁၈၂၄", "၁၈၅၂", "၁၈၈၅", "၁၉၄၈"],
    "correct": "၁၈၂၄"
},
{
    "question": "မြန်မာ့လွတ်လပ်ရေးနေ့မှာ မည်သည့်နေ့ဖြစ်သနည်း။",
    "options": ["ဇန်နဝါရီ ၄", "ဇူလိုင် ၁၉", "ဧပြီ ၁၇", "မေလ ၁"],
    "correct": "ဇန်နဝါရီ ၄"
},
{
    "question": "ဘိုးတော်ဦးအောင်ဆန်းကို မည်သည့်နေရာတွင် လုပ်ကြံခဲ့သည်။",
    "options": ["ဗိုလ်ချုပ်ရုံး", "ဗဟန်း", "ဗိုလ်တထောင်", "စစ်တက္ကသိုလ်"],
    "correct": "ဗိုလ်ချုပ်ရုံး"
},
{
    "question": "ဒုတိယအင်္ဂလိပ်မြန်မာစစ်ဖြစ်ပွားခဲ့သည့်နှစ်မှာ ဘယ်နှနှစ်လဲ။",
    "options": ["၁၈၅၂", "၁၈၂၄", "၁၈၈၅", "၁၉၃၀"],
    "correct": "၁၈၅၂"
},
{
    "question": "ကျော်ဟောကျော်ဖျော် သီချင်းကို မူလရေးသားသူမှာ ဘယ်သူလဲ။",
    "options": ["အောင်စိုး", "တင်မောင်", "မောင်သင်း", "ကြည်တော်"],
    "correct": "မောင်သင်း"
},
{
    "question": "ဧရာဝတီမြစ်သည် မြန်မာနိုင်ငံ၏ အဓိကမြစ်တစ်စင်းဖြစ်သည်။ ၎င်းသည် မည်သည့်တောင်တွင်မွေးဖွားသနည်း။",
    "options": ["မန်ဒလေးတောင်", "ဟိမဝန္တာတောင်", "ရှမ်းတောင်", "မထကတောင်"],
    "correct": "ဟိမဝန္တာတောင်"
},
{
    "question": "မြန်မာ့ပထမဆုံးသမ္မတသည် ဘယ်သူလဲ။",
    "options": ["သန်းထွေး", "နယ်ဝန်း", "ဘားမြန်", "အောင်ဆန်း"],
    "correct": "သန်းထွေး"
},
{
    "question": "ဧရာဝတီတိုင်း၏မြို့တော်မှာ ဘယ်မြို့လဲ။",
    "options": ["မော်လမြိုင်", "ပုသိမ်", "နေပြည်တော်", "တောင်ငူ"],
    "correct": "ပုသိမ်"
},
{
    "question": "မြန်မာ့ပထမဆုံးနိုင်ငံတော်ဝန်ကြီးချုပ်မှာ ဘယ်သူလဲ။",
    "options": ["ဦးနု", "သန်းထွေး", "အောင်ဆန်း", "ဦးချစ်"],
    "correct": "ဦးနု"
},
{
    "question": "မြန်မာနိုင်ငံသည် မည်သည့်တောင်ကြီးအဖွဲ့အစည်းတွင် ပါဝင်သည်။",
    "options": ["အရှေ့တောင်အာရှ", "အာဖရိက", "ဥရောပ", "အမေရိက"],
    "correct": "အရှေ့တောင်အာရှ"
},
{
    "question": "မြန်မာနိုင်ငံ၏အကြီးဆုံးတောင်မှာ ဘယ်တောင်လဲ။",
    "options": ["ချောင်းသီတောင်", "ခင်မောင်တောင်", "ဟခါဘူမတောင်", "မထကတောင်"],
    "correct": "မထကတောင်"
},
{
    "question": "မြန်မာနိုင်ငံမှာ ပထမဆုံးရှိခဲ့သော ဘုရင့်နိုင်ငံမှာ ဘာလဲ။",
    "options": ["ပုဂံ", "တောင်ငူ", "အင်းဝ", "တောင်သူ"],
    "correct": "ပုဂံ"
},
{
    "question": "တောင်ငူတွင် တည်ရှိသော နတ်မင်းကျောင်းဟု လူသိများသော ဘုရားမှာ ဘာလဲ။",
    "options": ["မဟာမြတ်မင်းဘုရား", "အင်းဝစေတီ", "ရွှေမင်းတုန်း", "ရွှေနန်းတော်"],
    "correct": "မဟာမြတ်မင်းဘုရား"
},
{
    "question": "ကော့သောင်းစစ်ကို မြန်မာဘုရင်မင်းသည် ဦးဆောင်ခဲ့သနည်း။",
    "options": ["အနော်ရထာ", "ဘုရင့်နောင်", "နောင်ဒုက္ခ", "မြန်မာမင်း"],
    "correct": "ဘုရင့်နောင်"
},
{
    "question": "မြန်မာ့အမျိုးသားသံတော်ဆင်၏အရောင်များမှာဘာတွေလဲ။",
    "options": ["အနီ၊ အဖြူ၊ အစိမ်း", "အနီ၊ အမဲ၊ အဝါ", "အနီ၊ အဖြူ၊ အပြာ", "အဝါ၊ အစိမ်း၊ အနီ"],
    "correct": "အနီ၊ အဖြူ၊ အစိမ်း"
},
{
    "question": "နိုင်ငံတော်သမ္မတကို ပြည်ထောင်စုလွှတ်တော်ကရွေးချယ်သည်။ ဒီအချက်ဟုတ်သလား။",
    "options": ["ဟုတ်သည်", "မဟုတ်ပါ", "တချို့ကသာ", "သိသလောက် မဟုတ်"],
    "correct": "ဟုတ်သည်"
},
{
    "question": "မြန်မာ့နိုင်ငံတော်နံပါတ် ၆၆၆ ဆိုတာ ဘာကိုဆိုလိုသနည်း။",
    "options": ["ဗျည်းနံပါတ်", "နိုင်ငံရေးစည်းမျဉ်း", "တပ်မတော်အမိန့်", "ဖုန်းနံပါတ်"],
    "correct": "တပ်မတော်အမိန့်"
},
{
    "question": "မင်းတွင်းမြို့ကို တည်ထောင်ခဲ့သောဘုရင်မှာ ဘယ်သူလဲ။",
    "options": ["မင်းဒင်မင်း", "စည်သူမင်း", "မင်းကောင်း", "သူနောင်မင်း"],
    "correct": "မင်းဒင်မင်း"
},
    {
        "question": "ဗမာ့အမျိုးသားရေးအဖွဲ့ (Dobama Asiayone) ကို မည်သည့်နှစ်တွင် တည်ထောင်ခဲ့သည်။",
        "options": ["၁၉၄၂", "၁၉၃၀", "၁၉၂၀", "၁၉၄၇"],
        "correct": "၁၉၃၀"
    },
    {
        "question": "အာဇာနည်နေ့ကို မည်သည့်ရက်တွင်ကျင်းပသည်။",
        "options": ["ဇူလိုင် ၁၉", "မေလ ၂၉", "ဧပြီ ၁၇", "ဩဂုတ် ၈"],
        "correct": "ဇူလိုင် ၁၉"
    },
    {
        "question": "မြန်မာ့လွတ်လပ်ရေးနေ့မှာ မည်သည့်နေ့ဖြစ်သနည်း။",
        "options": ["ဇန်နဝါရီ ၄", "ဇူလိုင် ၁၉", "ဧပြီ ၁၇", "မေလ ၁"],
        "correct": "ဇန်နဝါရီ ၄"
    },
    {
        "question": "အာဇာနည်နေ့ကို မည်သည့်ရက်တွင်ကျင်းပသည်။",
        "options": ["ဇူလိုင် ၁၉", "မေလ ၂၉", "ဧပြီ ၁၇", "ဩဂုတ် ၈"],
        "correct": "ဇူလိုင် ၁၉"
    },
    {
        "question": "ဗိုလ်ချုပ်အောင်ဆန်းကို မည်သည့်နှစ်တွင် လုပ်ကြံခံခဲ့ရသည်။",
        "options": ["၁၉၄၇", "၁၉၄၅", "၁၉၄၈", "၁၉၄၁"],
        "correct": "၁၉၄၇"
    },
    {
        "question": "မြန်မာနိုင်ငံကို ဘရိတိသျှ စတင်ကျူးကျော်ခဲ့သောနှစ်?",
        "options": ["၁၈၈၅", "၁၈၂၄", "၁၉၄၈", "၁၉၂၀"],
        "correct": "၁၈၂၄"
    },
    {
        "question": "မြန်မာ့လွတ်လပ်ရေးနေ့သည်?",
        "options": ["ဇန်နဝါရီ ၄", "မတ် ၂၇", "ဖေဖော်ဝါရီ ၁၂", "ဒီဇင်ဘာ ၂၅"],
        "correct": "ဇန်နဝါရီ ၄"
    },
    {
        "question": "အောင်ဆန်းဘုရင်အမည်မှာ?",
        "options": ["မင်းကွန်း", "ဧရာဝတီ", "မြဝတီ", "သန်းထွန်း"],
        "correct": "မင်းကွန်း"
    },
]

user_sessions = {}
leaderboard = {}

daily_challenge_data = {
    "date": None,
    "question": None,
    "participants": {}
}

# Store user IDs for sending messages to all users
user_ids = set()

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id  # Get user ID from the message sender

    # Add user ID to the user_ids set
    if user_id not in user_ids:
        user_ids.add(user_id)
    
    # Start message with mode options
    keyboard = [
        [InlineKeyboardButton("🎲 Random Mode", callback_data="mode_random")],
        [InlineKeyboardButton("🛡 Survival Mode", callback_data="mode_survival")],
        [InlineKeyboardButton("📅 Daily Challenge", callback_data="mode_daily")],
        [InlineKeyboardButton("⚔️ 1 v 1 Mode", callback_data="mode_1v1")],
        [InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("အောက်မှ mode ရွေးပါ:", reply_markup=reply_markup)

# Handle mode selection
async def choose_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    mode = query.data.split("_")[1]
    user_id = query.from_user.id

    if mode == "1v1":
        await query.message.reply_text("1 v 1 mode မကြာမီတွင်လာမည်!")
        return

    if mode == "daily":
        today = str(datetime.date.today())
        if daily_challenge_data["date"] != today:
            daily_challenge_data["date"] = today
            daily_challenge_data["question"] = random.choice(questions)
            daily_challenge_data["participants"] = {}

        if user_id in daily_challenge_data["participants"]:
            await query.message.reply_text("ယနေ့ Daily Challenge ကိုပြီးပြီးပါပြီ။ မနက်ဖြန်ပြန်လာပါ။")
            return

        user_sessions[user_id] = {
            "score": 0,
            "mode": mode,
            "question": daily_challenge_data["question"]
        }

        await send_daily_question(query.message.chat_id, context, user_id)
        return

    user_sessions[user_id] = {
        "score": 0,
        "mode": mode,
        "question": None
    }

    await query.message.reply_text(f"{mode.capitalize()} mode တွင်စတင်ပါမည်။")
    await ask_question(query.message.chat_id, context, mode, user_id)

# Ask question
async def ask_question(chat_id, context: ContextTypes.DEFAULT_TYPE, mode, user_id):
    question = random.choice(questions)
    user_sessions[user_id]['question'] = question
    buttons = [[InlineKeyboardButton(opt, callback_data=f"answer:{opt}")]
               for opt in question['options']]
    reply_markup = InlineKeyboardMarkup(buttons)
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"မေးခွန်း: {question['question']}",
        reply_markup=reply_markup
    )

# Handle normal answers
async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if user_id not in user_sessions:
        await query.message.reply_text("ကျေးဇူးပြု၍ /start ဖြင့်စတင်ပါ")
        return

    session = user_sessions[user_id]
    correct = session['question']['correct']
    chosen = query.data.split(":")[1]
    mode = session['mode']

    if chosen == correct:
        session['score'] += 1
        await query.message.reply_text("✔️ မှန်ပါတယ်!")

        if mode == "survival":
            await ask_question(query.message.chat_id, context, mode, user_id)
        else:
            next_button = InlineKeyboardMarkup([
                [InlineKeyboardButton("နောက်ထပ်မေးခွန်း", callback_data="next_random_question")]
            ])
            await query.message.reply_text("နောက်ထပ်မေးခွန်း:", reply_markup=next_button)
    else:
        await query.message.reply_text(f"❌အမှားဖြေခဲ့ပါသည်။ မှန်ကန်သောအဖြေမှာ: {correct}")
        if mode == "survival":
            await query.message.reply_text(f"Game Over!\nရမှတ်: {session['score']}")
            update_leaderboard(user_id, session['score'])
            del user_sessions[user_id]
            restart_button = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔁 Start Again (Survival Mode)", callback_data="mode_survival")]
            ])
            await query.message.reply_text("ထပ်မံစတင်လိုပါက:", reply_markup=restart_button)
        else:
            next_button = InlineKeyboardMarkup([
                [InlineKeyboardButton("နောက်ထပ်မေးခွန်း", callback_data="next_random_question")]
            ])
            await query.message.reply_text("နောက်ထပ်မေးခွန်း:", reply_markup=next_button)

# Daily challenge question
async def send_daily_question(chat_id, context: ContextTypes.DEFAULT_TYPE, user_id):
    q = daily_challenge_data["question"]
    buttons = [[InlineKeyboardButton(opt, callback_data=f"daily_answer:{opt}")]
               for opt in q['options']]
    markup = InlineKeyboardMarkup(buttons)
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"📅 Daily Challenge:\nမေးခွန်း - {q['question']}",
        reply_markup=markup
    )

# Handle daily answer
async def handle_daily_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if user_id not in user_sessions or user_sessions[user_id]['mode'] != "daily":
        await query.message.reply_text("Daily Challenge အတွက် /start ဖြင့်စတင်ပါ")
        return

    session = user_sessions[user_id]
    correct = session['question']['correct']
    chosen = query.data.split(":")[1]

    if user_id not in daily_challenge_data["participants"]:
        daily_challenge_data["participants"][user_id] = 1 if chosen == correct else 0

    if chosen == correct:
        await query.message.reply_text("✔️ မှန်ပါတယ်! မနက်ဖြန်ပြန်လာပါ။")
    else:
        await query.message.reply_text(f"❌ အမှားဖြေခဲ့သည်။ မှန်ကန်သောအဖြေမှာ: {correct}\nမနက်ဖြန်ပြန်ကြစို့!")

    del user_sessions[user_id]

# Next random question
async def handle_next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if user_id not in user_sessions:
        await query.message.reply_text("ကျေးဇူးပြု၍ /start ဖြင့်စတင်ပါ")
        return

    await ask_question(query.message.chat_id, context, user_sessions[user_id]['mode'], user_id)

# Update leaderboard
def update_leaderboard(user_id, score):
    if user_id in leaderboard:
        if score > leaderboard[user_id]:
            leaderboard[user_id] = score
    else:
        leaderboard[user_id] = score

# Show leaderboard
async def show_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    leaderboard_text = "🏆 Top 10 Players (Survival Mode Only):\n"
    sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)[:10]

    if sorted_board:
        for i, (user_id, score) in enumerate(sorted_board, 1):
            try:
                user = await context.bot.get_chat(user_id)
                name = f"@{user.username}" if user.username else user.full_name
            except:
                name = f"User {user_id}"
            leaderboard_text += f"{i}. {name} - {score} မှန်ခဲ့သည်\n"
    else:
        leaderboard_text += "အချက်အလက်မရှိသေးပါ။"

    await update.callback_query.message.reply_text(leaderboard_text)

# Send text message to all users
async def send_text_to_users(context: ContextTypes.DEFAULT_TYPE, message: str):
    for user_id in user_ids:
        try:
            print(f"Attempting to send message to {user_id}")  # Debugging line
            await context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"Failed to send message to {user_id}: {e}")

# Command to send text message to all users
async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    owner_id = "1896158899"  # Replace with your user ID
    if update.message.from_user.id != int(owner_id):
        await update.message.reply_text("You are not authorized to send messages.")
        return

    message = update.message.text.split(' ', 1)[1]  # Get the message part after the command (e.g., /send_message hi)
    print(f"Broadcast message: {message}")  # Debugging line
    await send_text_to_users(context, message)
    await update.message.reply_text("Text message sent to all users!")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(choose_mode, pattern="^mode_"))
    app.add_handler(CallbackQueryHandler(handle_answer, pattern="^answer:"))
    app.add_handler(CallbackQueryHandler(handle_daily_answer, pattern="^daily_answer:"))
    app.add_handler(CallbackQueryHandler(handle_next_question, pattern="^next_random_question$"))
    app.add_handler(CallbackQueryHandler(show_leaderboard, pattern="^leaderboard$"))
    app.add_handler(CommandHandler("send_message", send_message))  # Command to send text message

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()