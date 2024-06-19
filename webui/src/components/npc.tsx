"use client";
import React from "react";
import ImageDisplayComponent from "@/components/ImageDisplayComponent";
import NPCAnswer from "@/components/npc-answer";

export default function NPC(props: { imagePath: string }) {
  return (
    <div className="flex relative min-h-screen">
      <div className="flex flex-col items-center justify-center w-full">
        <div className="relative flex justify-center items-center w-full">
          <ImageDisplayComponent src={props.imagePath} />
          <div className="relative">
            <NPCAnswer />
          </div>
        </div>
      </div>
    </div>
  );
}
