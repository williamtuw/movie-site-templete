import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "greenweb.settings")


def main():

    from pages.models import Video
    # with open("info_extra.txt","r",encoding="utf-8") as fp:
    #     video_dict = {case.split("****")[0]:{"title":case.split("****")[1],"img_link":case.split("****")[2]} for case in fp}
    #     with open("movie_link_extra.txt","r",encoding="utf-8")as fp2:
    #         for case in fp2:
    #             video_dict.get(case.split("****")[0])["video_url"] = case.split("****")[1].strip()
    #
    # video_case_list = []
    #
    # for k,v in video_dict.items():
    #     if v.get("video_url",None):
    #         video_case_list.append(v)

    # video_list = [Video(title=case["title"],img_link=case["img_link"],video_url=case["video_url"]) for case in video_case_list]

    video_list = [Video(title="https://this the {}th video".format(i), img_link="https://img{}.png".format(i), video_url="https://video{}.mp4".format(i)) for i in
                  range(1000)]
    Video.objects.bulk_create(video_list)


if __name__ == "__main__":
    main()
    print('Done!')