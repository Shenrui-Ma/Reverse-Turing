import Link from "next/link";
import Image from "next/image";
import Sidebar from "@/components/item-sidebar";
import ItemAuthor from "@/components/item-author";
import ButtonShare from "@/components/button-share";

export default function HomePage() {
  return (
    <div className="flex">
      {/* 侧边栏 */}
      {/* 分享按钮 */}
      <ButtonShare />

      {/* 主内容区 */}
      <div className="flex-grow">
        <div className="flex justify-center ">
          <div className="text-2xl mt-8 border p-8 border-black rounded-md bg-blue-200 font-bold font-serif ">
            目前只开发了4人编程问答和4人原神角色扮演
            <div className="flex justify-center items-center">
              <Image
                src="/images/aelecchino_full.png"
                alt="四倍体果蝇 Azrael-76"
                width={450}
                height={750}
              />
            </div>
          </div>
        </div>

        <div className="flex justify-center items-center mt-8 w-screen button-hover-effect relative">
          <div className="flex justify-center items-center space-x-4">
            <Link
              href="/coding_questions_4p"
              className="bg-red-200 h-20 w-36 rounded-md flex justify-center items-center border-4 border-red-950"
            >
              4人编程问题问答
            </Link>
            <Link
              href="/genshin_roleplay_4p"
              className="bg-red-200 h-20 w-36 rounded-md flex justify-center items-center border-4 border-red-950"
            >
              4人原神角色扮演
            </Link>
          </div>
        </div>
      </div>
      <Sidebar />
      <ItemAuthor />
    </div>
  );
}
