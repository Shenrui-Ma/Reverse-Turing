import React, { useContext } from "react";
import { MessageContext, MessageContextType } from "./MessageContext";
import CodeBlock from "./code-block";

function NPCAnswer() {
  const context = useContext(MessageContext);

  if (!context) {
    return null; // 或者返回一个加载状态
  }

  const { message } = context as MessageContextType;

  const renderContent = (text: string) => {
    const parts = text.split(/(```[\s\S]*?```)/g); // 使用正则表达式分割文本
    console.log("Parts:", parts); // 打印 parts 数组
    return parts.map((part, index) => {
      if (part.startsWith("```") && part.endsWith("```")) {
        const code = part.slice(3, -3).trim(); // 去除反引号并去除首尾空白
        return <CodeBlock key={index} code={code} />;
      }
      return <p key={index}>{part}</p>;
    });
  };

  return (
    <div
      className="border-8 border-amber-500 rounded-lg p-4 m-4 bg-amber-100"
      style={{
        width: "250px",
        height: "425px",
        overflow: "auto",
        fontSize: "18px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      {message ? renderContent(message) : "Waiting for question..."}
    </div>
  );
}

export default NPCAnswer;
