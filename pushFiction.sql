CREATE DATABASE `fiction` CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `fiction`;
-- ----------------------------
-- Table structure for `novelinfo` 小说简介信息
-- ----------------------------
DROP TABLE IF EXISTS `novelinfo`;
CREATE TABLE `novelinfo` (
  `novel_id` int(32) NOT NULL,
  `novel_url` varchar(100) NOT NULL,
  `novel_name` varchar(50) DEFAULT NULL,##小说名
  `author` varchar(30) DEFAULT NULL,##作者名
  `description` text DEFAULT NULL,##小说简介
  `type` varchar(20) DEFAULT NULL,##分类
  `lastchapter` varchar(100) DEFAULT NULL,##最新章节名
  `chaptercount` int(11) DEFAULT NULL,##章节数
  `wordcount` int(11) DEFAULT NULL,##字数
  `keywords` varchar(100) DEFAULT NULL,##关键字
  `createtime` bigint(20) DEFAULT NULL,##创建时间
  `updatetime` bigint(20) DEFAULT NULL,##最后更新时间
  PRIMARY KEY (`novel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for `novelchapter` 小说章节信息
-- ----------------------------
DROP TABLE IF EXISTS `novelchapter`;
CREATE TABLE `novelchapter` (
  `chapter_id` int(32) NOT NULL auto_increment,
  `novel_id` int(32) NOT NULL,
  `chapter_url` varchar(100) NOT NULL,##阅读页URL
  `chapter_real_id` int(32) NOT NULL,##在笔趣阁中的章节id号
  `chapter_title` varchar(50) DEFAULT NULL,##章节名
  `wordcount` int(11) DEFAULT NULL,##字数
  `chaptertime` bigint(20) DEFAULT NULL,##章节时间
  `createtime` bigint(20) DEFAULT NULL,##创建时间
  PRIMARY KEY (`chapter_id`),
  CONSTRAINT `first` FOREIGN KEY (`novel_id`) REFERENCES `novelinfo` (`novel_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for `novelchapterdetail` 小说章节详细信息
-- ----------------------------
DROP TABLE IF EXISTS `novelchapterdetail`;
CREATE TABLE `novelchapterdetail` (
  `content_id` int(32) NOT NULL auto_increment,
  `novel_id` int(32) NOT NULL,
  `chapter_id` int(32) NOT NULL,
  `content_url` varchar(100) NOT NULL,##阅读页url
  `title` varchar(50) DEFAULT NULL,##章节标题
  `wordcount` int(11) DEFAULT NULL,##字数
  `chapterid` int(11) DEFAULT NULL,##章节排序
  `content` text,##正文
  `chaptertime` bigint(20) DEFAULT NULL,##章节时间
  `createtime` bigint(20) DEFAULT NULL,##创建时间
  `updatetime` bigint(20) DEFAULT NULL,##最后更新时间
  PRIMARY KEY (`content_id`),
  CONSTRAINT `second` FOREIGN KEY (`novel_id`) REFERENCES `novelinfo` (`novel_id`) ON DELETE CASCADE,
  CONSTRAINT `third` FOREIGN KEY (`chapter_id`) REFERENCES `novelchapter` (`chapter_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert  into novelinfo (novel_id, novel_url, novel_name)
values
(35569, "http://www.biquge.com.cn/book/35569/", "同桌凶猛"),
(34197, "http://www.biquge.com.cn/book/34197/", "民国谍影");