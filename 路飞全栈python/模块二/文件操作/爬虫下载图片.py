import  requests

res = requests.get("https://na-nikke-aws.playerinfinite.com/cms/nrft/feeds/pic/_dcba96950c256305b2cf2943f18936f3dbe16734-3840x2160-ori_s_80_50_ori_q_80.webp")
print(res.content)

with open("nikke.jpg", "wb") as f:
    f.write(res.content)