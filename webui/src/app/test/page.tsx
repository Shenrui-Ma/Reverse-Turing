"use client";
import NPC from "@/components/npc";
import Player from "@/components/player";
import BarQuestion from "@/components/bar-question";
import { MessageProvider } from "@/components/MessageContext";

export default function TestPage() {
  const imagePaths = [
    "/images/hutao.png",
    "/images/chiori.png",
    "/images/arlecchino.png",
  ];

  return (
    <MessageProvider>
      <div className="flex justify-center items-center">
        <BarQuestion question_type="我需要你作为一个出题人，随机生成一个和编程知识有关的问题。" />
      </div>
    </MessageProvider>
  );
}
