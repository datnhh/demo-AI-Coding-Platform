using Demo;

using Xunit;

namespace Demo.Tests;

public sealed class StringUtilsTests
{
    [Fact]
    public void Reverse_DaoNguocChuoi() => Assert.Equal("cba", StringUtils.Reverse("abc"));

    [Fact]
    public void Reverse_ChuoiRong_TraVeChuoiRong() => Assert.Equal(string.Empty, StringUtils.Reverse(""));

    [Fact]
    public void Reverse_Null_NemArgumentNullException() =>
        Assert.Throws<ArgumentNullException>(() => StringUtils.Reverse(null!));

    [Fact]
    public void IsPalindrome_ChuoiDoiXung_TraVeTrue() => Assert.True(StringUtils.IsPalindrome("madam"));

    [Fact]
    public void IsPalindrome_ChuoiDoiXungCoHoaThuongVaKhoangTrang_TraVeTrue() =>
        Assert.True(StringUtils.IsPalindrome("Race car"));

    [Fact]
    public void IsPalindrome_ChuoiKhongDoiXung_TraVeFalse() => Assert.False(StringUtils.IsPalindrome("abc"));

    [Fact]
    public void IsPalindrome_ChuoiRong_TraVeTrue() => Assert.True(StringUtils.IsPalindrome(""));

    [Fact]
    public void IsPalindrome_Null_NemArgumentNullException() =>
        Assert.Throws<ArgumentNullException>(() => StringUtils.IsPalindrome(null!));

    [Theory]
    [InlineData("Xin chào Việt Nam", "Xin chao Viet Nam")]
    [InlineData("ĐẠI HỌC BÁCH KHOA", "DAI HOC BACH KHOA")]
    [InlineData("Ăn quả nhớ kẻ trồng cây", "An qua nho ke trong cay")]
    [InlineData("đường đời tấp nập", "duong doi tap nap")]
    [InlineData("Lập trình C#", "Lap trinh C#")]
    public void RemoveDiacritics_TiengVietCoDau_TraVeKhongDau(string input, string expected) =>
        Assert.Equal(expected, StringUtils.RemoveDiacritics(input));

    [Fact]
    public void RemoveDiacritics_ChuoiRong_TraVeChuoiRong() =>
        Assert.Equal(string.Empty, StringUtils.RemoveDiacritics(string.Empty));

    [Fact]
    public void RemoveDiacritics_Null_NemArgumentNullException() =>
        Assert.Throws<ArgumentNullException>(() => StringUtils.RemoveDiacritics(null!));
}
