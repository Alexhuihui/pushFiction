CREATE DATABASE `fiction` CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `fiction`;

DROP TABLE IF EXISTS `novelinfo`;
CREATE TABLE `novelinfo` (
  `novel_id` int(32) NOT NULL,
  `novel_url` varchar(100) NOT NULL,
  `novel_name` varchar(50) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `lastchapter` varchar(100) DEFAULT NULL,
  `chaptercount` int(11) DEFAULT NULL,
  `wordcount` int(11) DEFAULT NULL,
  `keywords` varchar(100) DEFAULT NULL,
  `createtime` bigint(20) DEFAULT NULL,
  `updatetime` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`novel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `novelchapter`;
CREATE TABLE `novelchapter` (
  `chapter_id` int(32) NOT NULL auto_increment,
  `novel_id` int(32) NOT NULL,
  `chapter_url` varchar(100) NOT NULL,
  `chapter_real_id` int(32) NOT NULL,
  `chapter_title` varchar(50) DEFAULT NULL,
  `wordcount` int(11) DEFAULT NULL,
  `chaptertime` bigint(20) DEFAULT NULL,
  `createtime` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`chapter_id`),
  CONSTRAINT `first` FOREIGN KEY (`novel_id`) REFERENCES `novelinfo` (`novel_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `novelchapterdetail`;
CREATE TABLE `novelchapterdetail` (
  `content_id` int(32) NOT NULL auto_increment,
  `novel_id` int(32) NOT NULL,
  `chapter_id` int(32) NOT NULL,
  `content_url` varchar(100) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `wordcount` int(11) DEFAULT NULL,
  `chapterid` int(11) DEFAULT NULL,
  `content` text,
  `chaptertime` bigint(20) DEFAULT NULL,
  `createtime` bigint(20) DEFAULT NULL,
  `updatetime` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`content_id`),
  CONSTRAINT `second` FOREIGN KEY (`novel_id`) REFERENCES `novelinfo` (`novel_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert  into novelinfo (novel_id, novel_url, novel_name)
values
(35569, "http://www.biquge.com.cn/book/35569/", "同桌凶猛"),
(34197, "http://www.biquge.com.cn/book/34197/", "民国谍影"),
(30152, "http://www.biquge.com.cn/book/30152/", "反叛的大魔王"),
(33710, "http://www.biquge.com.cn/book/33710/", "我要出租自己"),
(32697, "http://www.biquge.com.cn/book/32697/", "大医凌然"),
(34420, "http://www.biquge.com.cn/book/34420/", "我的女友真是大明星"),
(36825, "http://www.biquge.com.cn/book/36825/", "龙族Ⅴ：悼亡者的归来"),
(32460, "http://www.biquge.com.cn/book/32460/", "我真的长生不老"),
(35016, "http://www.biquge.com.cn/book/35016/", "我真不是神仙"),
(36681, "http://www.biquge.com.cn/book/36681/", "斗罗大陆IV终极斗罗"),
(30594, "http://www.biquge.com.cn/book/30594/", "凡人修仙之仙界篇");