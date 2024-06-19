"use client";
import NPC from "@/components/npc";
import Player from "@/components/player";
import BarQuestion from "@/components/bar-question";
import { MessageProvider } from "@/components/MessageContext";

export default function CodingQuestions4pPage() {
  const imagePaths = [
    "/images/hutao.png",
    "/images/chiori.png",
    "/images/arlecchino.png",
  ];

  return (
    <div className="flex flex-col h-full">
      <div className="fixed top-0 left-0 w-full z-50">
        <MessageProvider>
          <BarQuestion question_type="我需要你随机生成一个和计算机有关的问题（包括c语言、c++、python、面向对象编程、数据结构与算法、机器学习、深度学习），并返回一个30个汉字内的问题（数字，字母等其他符号的字数不作限制），要求出简答题，考理论知识，不出现场编程题。如果出选择题，要给全选项。" />
        </MessageProvider>
      </div>
      <div className="flex justify-center items-center h-screen mt-[-15vh]">
        {imagePaths.map((path, index) => (
          <MessageProvider key={index}>
            <NPC imagePath={path} />
          </MessageProvider>
        ))}
      </div>
      <div className="flex relative justify-center mt-[-55vh]">
        <Player imagePath="/images/罗志勇3.png" />
      </div>
    </div>
  );
}
